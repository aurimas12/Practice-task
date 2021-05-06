#!/bin/bash
echo "Hello World"

# Create workspace
curl -i -X POST http://localhost:8001/workspaces \
--data "name=team-a"

# Create service
curl -i -X POST http://localhost:8001/services/ \
--data name=mockbin \
--data url=http://mockbin.org/request

# Create route
curl -i -X POST http://localhost:8001/team-a/services/mockbin/routes \
--data "name=mockbin" \
--data "paths[]=/mockbin"

# Enable the OAuth 2.0 plugin for that service
curl -i -X POST localhost:8001/team-a/services/mockbin/plugins \
--data "name=oauth2" \
--data "config.scopes=email" \
--data "config.enable_client_credentials=true"

# Create consumer
curl -i -X POST localhost:8001/team-a/consumers \
--data "username=user1"

# Create a key for that consumer
curl -i -X POST localhost:8001/team-a/consumers/user1/key-auth \
--data "key=123"

# You can then provision new OAuth 2.0 credentials (also called “OAuth applications”) by making the following HTTP request
curl -i -X POST http://localhost:8001/team-a/consumers/user1/oauth2 \
--data "name=demo" \
--data "client_id=456" \
--data "client_secret=789" \
--data "redirect_uris=http://mockbin.org/"
