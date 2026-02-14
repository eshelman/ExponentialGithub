#!/usr/bin/env bash
# Fetch daily GitHub contribution counts for a user via the GraphQL API.
# Requires: gh (GitHub CLI), jq
# Usage: ./fetch_contributions.sh [username] [start_year] [end_year]

set -euo pipefail

USERNAME="${1:-eshelman}"
START_YEAR="${2:-2020}"
END_YEAR="${3:-2026}"

# Build aliased GraphQL query — one alias per year
QUERY="query {"
for year in $(seq "$START_YEAR" "$END_YEAR"); do
  next=$((year + 1))
  QUERY+="
  y${year}: user(login: \"${USERNAME}\") {
    contributionsCollection(from: \"${year}-01-01T00:00:00Z\", to: \"${next}-01-01T00:00:00Z\") {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }"
done
QUERY+="
}"

# Run the query and flatten + deduplicate by date
gh api graphql -f query="$QUERY" | jq -r '
  [.data | to_entries[] | .value.contributionsCollection.contributionCalendar.weeks[].contributionDays[]]
  | group_by(.date)
  | map(.[0])
  | sort_by(.date)
' > contributions.json

echo "Saved $(jq length contributions.json) daily entries to contributions.json"
