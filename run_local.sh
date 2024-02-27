export ENVIRONMENT="${1?Please define the environment}"
export RUN_TIME="${2:-10s}"
export THREAD_COUNT="${3:-1}"

echo
echo "ENVIRONMENT: ${ENVIRONMENT}"
echo "RUN_TIME: ${RUN_TIME}"
echo "THREAD_COUNT: ${THREAD_COUNT}"
echo

locust --config ./locust.conf --users ${THREAD_COUNT} --spawn-rate ${THREAD_COUNT} --run-time ${RUN_TIME} --env ${ENVIRONMENT}