namespace=${1}

usage() {
    cat <<EOF
usage: ${0} <namespace>
EOF
    exit 1
}

if [[ -z $namespace ]]; then
    usage
fi

kubectl -n $namespace delete configmap pycode-review
kubectl -n $namespace create configmap pycode-review --from-file=../review.py
kubectl -n $namespace delete -f deploy.yaml
kubectl -n $namespace apply -f deploy.yaml
