#!/bin/bash
echo "Hello World"

# Create service
curl -i -X POST http://localhost:8001/services/ \
--data name=mockbin \
--data url=http://mockbin.org/request