#!/bin/bash

# Create service
curl -i -X POST http://localhost:8001/services/ \
--data name=api \
--data host=django \
--data port=1337 \
--data path=/


