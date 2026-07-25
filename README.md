# S283 owned fork-SHA checkout control

This public repository is an inert, researcher-owned GitHub Actions fixture. It reproduces one
question from `snowflakedb/snowflake-sqlalchemy`: can a base-repository `workflow_dispatch` run
`actions/checkout@v6` with an exact external pull-request head SHA while leaving `repository:`
unset?

The workflow has no secrets, OIDC permission, Snowflake credentials, artifact upload, cache, write
token, or release/deployment authority.

