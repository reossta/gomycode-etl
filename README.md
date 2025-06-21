# GoMyCode – DataOps Internship

→ Pipeline Description and Purpose
The pipeline processes subscription data to:

Clean and normalize date and percentage columns
Derive new fields such as SubscriptionMonth and estimated revenue
Output a cleaned dataset (cleaned_output.csv) ready for OLAP analysis
This helps analyze trends over time and understand revenue performance.

→ Graph Schema Design (Neo4j)
We used Neo4j to model relationships between:

Users (with or without a diploma)
Tracks (subscribed content)
Subscriptions (linking users to tracks, with progress info)
The graph schema makes it easy to query:

Completion trends
Diploma-based comparisons
Track popularity
See: graph/neo4j_graph_schema.png

→ Query Objectives (Cypher & SQL)

Cypher queries:
Top completed tracks
Diploma vs non-diploma user analysis
Schedule-based revenue insights
SQL queries (optional):
Monthly cohort analysis
Aggregated revenue by product type
See: graph/cypher_queries.txt

→ Key Assumptions and Design Choices

Used a default revenue of 100 when product schedule was missing
Removed percentage signs from the progress field for numeric conversion
Converted dates to monthly periods using to_period("M")
Structured folders into data/, images/, graph/ for clarity
Neo4j queries and schema were written but not run live
