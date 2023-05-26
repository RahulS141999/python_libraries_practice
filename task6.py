#pod1.yaml
'''apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: myapp
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80'''

#python_pods_display.py
import pykube
from pykube.objects import Pod

config = pykube.KubeConfig.from_file("/root/.kube/config")

config.set_current_context("gke_my-project1-383007_us-central1-a_cluster-1")
api = pykube.HTTPClient(config)

try:
    #pod = Pod.objects(api)
    #pod = pykube.Pod.objects(api).filter(namespace= "default", field_selector={"metadata.name":"nginx"}).get()
    #pod= pykube.Pod.objects(api).get_by_name(name= "nginx", namespace= "default")
    
    if pod:
        print("Pod found")
        print(pod.obj)
    else:
        print("Pod not found")

except pykube.exceptions.HTTPError as e:
    print(f"error: {e}")





'''class KubeConfigs(object):
    def __init__(self):
        try:
            self.api = HTTPClient(KubeConfig.from_file(filename="~/.kube/config"))

        except Exception as e:

logger.error("Kubernetes Cluster Connection error:", e)


def pod_status(self, namespace: str = pykube.all):

    self.namespace = namespace


if self.namespace == "all":

namespace = pykube.all

pod_dict = {}

for pod in Pod.objects(self.api).filter(namespace):

pod_dict[pod.name] = {pod.obj["status"]["phase"]}

return pod_dict


config = KubeConfig.from_file("~/.kube/config")

namespace = "default"

pod = Pod.objects(api=config.api, namespace=namespace)

for pod in pod:
    print(pod.name)'''

#python_script.py

from pykube import KubeConfig, HTTPClient
from pykube.objects import Pod 

config = KubeConfig.from_file("/root/.kube/config")

client = HTTPClient(config)

for pods in Pod.objects(client):
        print(pods)




'''
#import operator
#import pykube

api = pykube.HTTPClient(pykube.KubeConfig.from_file("~/.kube/config"))
#pods = pykube.Pod.objects(api).filter(namespace="default")
pods = pykube.Pod.objects(api).get()
ready_pods = filter(operator.attrgetter("ready"), pods)'''
