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

kubectl -n $namespace delete configmap pycode-detail
kubectl -n $namespace create configmap pycode-detail --from-file=../detail.py
kubectl -n $namespace delete configmap pycode-detail_v2
kubectl -n $namespace create configmap pycode-detail_v2 --from-file=../detail_v2.py
kubectl -n $namespace delete -f deploy.yaml
kubectl -n $namespace apply -f deploy.yaml
