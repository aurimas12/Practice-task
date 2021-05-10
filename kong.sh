#!/bin/bash
# Create service
curl -X POST http://kong:8001/services/ \
--data "name=booking" \
--data "host=django" \
--data "port=1337" \
--data "path=/" 
# Create route
curl -i -X POST http://kong:8001/services/booking/routes \
--data 'methods[]=GET' \
--data 'name=booking-routes'
# Enable the OAuth 2.0 plugin for that service
curl -i -X POST http://kong:8001/services/booking/plugins \
--data "name=oauth2" \
--data "config.scopes=email" \
--data "config.enable_client_credentials=true"
# Create consumer
curl -i -X POST http://kong:8001/consumers \
--data "username=user1"
# Create a key for that consumer
curl -i -X POST http://kong:8001/consumers/user1/key-auth \
--data "key=123"
# You can then provision new OAuth 2.0 credentials (also called “OAuth applications”) by making the following HTTP request
curl -i -X POST http://kong:8001/consumers/user1/oauth2 \
--data "name=demo" \
--data "client_id=456" \
--data "client_secret=789" \
--data "redirect_uris=http://localhost:8000/api/"