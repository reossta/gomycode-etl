# GoMyCode – DataOps Internship


### What is your data pipeline doing and why?

The pipeline processes subscription data to:
- Clean and normalize date and percentage columns
- Derive new fields such as `SubscriptionMonth` and estimated revenue
- Output a cleaned dataset (`cleaned_output.csv`) ready for OLAP analysis

This helps analyze trends over time and understand revenue performance.

### How did you design your graph schema?

We used Neo4j to model relationships between:
- Users (with or without a diploma)
- Tracks (subscribed content)
- Subscriptions (linking users to tracks, with progress info)

The graph schema makes it easy to query:
- Completion trends
- Diploma-based comparisons
- Track popularity

See: `graph/neo4j_graph_schema.png`

### What are your Cypher and SQL queries solving?

- Cypher queries address:
  - Top completed tracks
  - Diploma vs non-diploma user analysis
  - Schedule-based revenue insights

- SQL queries (optional) focus on:
  - Monthly cohort analysis
  - Aggregated revenue by product type

See: `graph/cypher_queries.txt`

### Assumptions, challenges, or design decisions

- Used a default revenue of 100 when product schedule was missing
- Removed percentage signs from progress field for conversion
- Converted dates to monthly periods using `to_period("M")`
- Chose simple file structure with folders: `data/`, `images/`, `graph/`
- Neo4j was not executed live; schema and queries are documented only
