# Build
```docker buildx build -t prefect --platform=linux/amd64 .```

# Run Orion Server
```docker-compose --profile orion up```

# Run Orion Server with Agent
```docker-compose --profile agent up```

# Run prefect Cli
```docker-compose run cli```

# Create Deployment
```prefect deployment build -n default -q default -a filename:functionname --rrule 'RRULE:FREQ=DAILY;COUNT=7;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9'```