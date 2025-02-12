#!/bin/bash

set -e
DEPLOYMENT_NAME="myapp"
while true; do
  STATUS=$(kubectl get deployment $DEPLOYMENT_NAME -o=jsonpath='{.status.conditions[?(@.type=="Available")].status}')
  if [[ "$STATUS" != "True" ]]; then
    echo "⚠️ Deployment failed! Rolling back..."
    kubectl rollout undo deployment/$DEPLOYMENT_NAME
  fi
  sleep 60  # Check every 60 seconds
done
    