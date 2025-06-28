/ [Home](index.md)

## Azure Container Apps

**Updated:** Sep 17, 2024



### How to push a local app to Docker public registry
```
Git repo:
https://github.com/kactlabs/simple-flask
git clone git@github.com:kactlabs/simple-flask.git


v1:

	docker build -t rj-server:v1 .
	docker run -p 9090:5000 --name rj-server-112 rj-server:v1

	http://0.0.0.0:9090/


	Push to DockerHub:

		docker build -t rj-server:v1 .

		docker tag rj-server:v1 rajacsp/rj-server:v1

		docker push rajacsp/rj-server:v1
```


### How to pull from public Docker
```
docker pull rajacsp/csp-server:v1
docker run -p 9090:5000 --name csp-server-112 rajacsp/csp-server:v1
```


```
Microservice: Server:

OS env variables:
RESOURCE_GROUP="rjresroucegroup"
LOCATION="centralindia"
CONTAINERAPPS_ENVIRONMENT="rjresroucegroup-env"
CONTAINERAPPS_NAME="rj-server"
ACR_BASE="rjsimpleflask"
REPOSITORY_NAME="rj-flask-server"
SUBSCRIPTION_ID="965..00f8d0"

echo $RESOURCE_GROUP
echo $LOCATION
echo $CONTAINERAPPS_NAME
echo $REPOSITORY_NAME
```



```
v1:

	docker build -t rj-server:v1 .
	docker run -p 9090:5000 --name rj-server-112 rj-server:v1

	http://0.0.0.0:9090/


	Push to DockerHub:

		docker build -t rj-server:v1 .

		docker tag rj-server:v1 rajacsp/rj-server:v1

		docker push rajacsp/rj-server:v1


	Login to ACR:

		az login
		az acr login --name $ACR_BASE


	Push to ACR:

		docker tag rj-server:v1 rjsimpleflask.azurecr.io/rj-flask-server:v1

		docker push rjsimpleflask.azurecr.io/rj-flask-server:v1




v2:

	Push to DockerHub:

		docker build -t rj-server:v2 .

		docker tag rj-server:v2 rajacsp/rj-server:v2

		docker push rajacsp/rj-server:v2


	Login to ACR:

		az login
		az acr login --name $ACR_BASE


	Push to ACR:

		docker tag rj-server:v2 rjsimpleflask.azurecr.io/rj-flask-server:v2

		docker push rjsimpleflask.azurecr.io/rj-flask-server:v2
```



```
az login
az acr login --name $ACR_BASE

# Create Container App Environment
az containerapp env create -n $CONTAINERAPPS_ENVIRONMENT -g $RESOURCE_GROUP \
    --location $LOCATION

#
verify:
az containerapp env list --resource-group $RESOURCE_GROUP

# how to create a container app
az containerapp up \
	  --name $CONTAINERAPPS_NAME \
	  --resource-group $RESOURCE_GROUP \
	  --location $LOCATION \
	  --environment $CONTAINERAPPS_ENVIRONMENT \
	  --image $ACR_BASE.azurecr.io/$REPOSITORY_NAME:v1 \
	  --target-port 5000 \
	  --ingress external \
	  --query properties.configuration.ingress.fqdn


	# verify
	az containerapp logs show -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP --type system --tail 50

	az containerapp show -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP

# Check revision
az containerapp revision list \
  --name $CONTAINERAPPS_NAME \
  --resource-group $RESOURCE_GROUP \
  -o table



# Adding Label to the recent revision
az containerapp revision label add -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP --label v1 --revision latest

# Update existing containerapp
az containerapp update \
  --container-name $CONTAINERAPPS_NAME \
  --name $CONTAINERAPPS_NAME \
  --resource-group $RESOURCE_GROUP \
  --image $ACR_BASE.azurecr.io/$REPOSITORY_NAME:v1 \
  --min-replicas 1 \
  --max-replicas 5 \
  --query properties.configuration.ingress.fqdn

# Change revision mode
az containerapp revision set-mode \
  --name $CONTAINERAPPS_NAME \
  --resource-group $RESOURCE_GROUP \
  --mode multiple

# Split traffic
az containerapp ingress traffic set \
    --name $CONTAINERAPPS_NAME \
    --resource-group $RESOURCE_GROUP \
    --label-weight label90=0 v1-1=0 v2-1=80 label12=20

    https://learn.microsoft.com/en-us/azure/container-apps/traffic-splitting?pivots=azure-cli


V2:

	# Update existing containerapp with v2
	az containerapp update \
	  --container-name $CONTAINERAPPS_NAME \
	  --name $CONTAINERAPPS_NAME \
	  --resource-group $RESOURCE_GROUP \
	  --image $ACR_BASE.azurecr.io/$REPOSITORY_NAME:v2 \
	  --min-replicas 1 \
	  --max-replicas 5 \
	  --revision-suffix v2 \
	  --query properties.configuration.ingress.fqdn


	# Adding Label to the recent revision
	az containerapp revision label add -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP --label v2 --revision latest


	# Split traffic
	az containerapp ingress traffic set \
	    --name $CONTAINERAPPS_NAME \
	    --resource-group $RESOURCE_GROUP \
	    --label-weight v1=80 v2=20

	verify:
	?


V3:

	# Push to ACR:
	docker build -t rj-server:v3 .

	docker tag rj-server:v3 rjsimpleflask.azurecr.io/rj-flask-server:v3

	docker push rjsimpleflask.azurecr.io/rj-flask-server:v3

	# Update existing containerapp with v3
	az containerapp update \
	  --container-name $CONTAINERAPPS_NAME \
	  --name $CONTAINERAPPS_NAME \
	  --resource-group $RESOURCE_GROUP \
	  --image $ACR_BASE.azurecr.io/$REPOSITORY_NAME:v3 \
	  --min-replicas 1 \
	  --max-replicas 5 \
	  --revision-suffix v3 \
	  --query properties.configuration.ingress.fqdn

	  verify:
	  ?


	# Adding Label to the recent revision
	az containerapp revision label add -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP --label v3 --revision latest


	# Split traffic
	az containerapp ingress traffic set \
	    --name $CONTAINERAPPS_NAME \
	    --resource-group $RESOURCE_GROUP \
	    --label-weight v2=80 v3=20



	# deactivate
	az containerapp revision deactivate --revision $CONTAINERAPPS_NAME--if8rxli \
                                    --name $CONTAINERAPPS_NAME \
                                    --resource-group $RESOURCE_GROUP


		https://learn.microsoft.com/en-us/cli/azure/containerapp/revision?view=azure-cli-latest#az-containerapp-revision-deactivate



V4:

	# Push to ACR:
	docker build -t rj-server:v4 .

	docker tag rj-server:v4 rjsimpleflask.azurecr.io/rj-server:v4

	docker push rjsimpleflask.azurecr.io/rj-server:v4

	# Update existing containerapp with v4
	az containerapp update \
	  --container-name $CONTAINERAPPS_NAME \
	  --name $CONTAINERAPPS_NAME \
	  --resource-group $RESOURCE_GROUP \
	  --image $ACR_BASE.azurecr.io/$REPOSITORY_NAME:v4 \
	  --min-replicas 1 \
	  --max-replicas 5 \
	  --revision-suffix v4 \
	  --query properties.configuration.ingress.fqdn

	  verify:
	  ?


	# Adding Label to the recent revision
	az containerapp revision label add -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP --label v4 --revision latest


	# Split traffic
	az containerapp ingress traffic set \
	    --name $CONTAINERAPPS_NAME \
	    --resource-group $RESOURCE_GROUP \
	    --label-weight v3=70 v4=30
```


```
Microservice: Client

Client:


RESOURCE_GROUP="rjresroucegroup"
LOCATION="centralindia"
CONTAINERAPPS_ENVIRONMENT="rjresroucegroup-env"
CONTAINERAPPS_NAME="rj-client"
ACR_BASE="rjsimpleflask"
REPOSITORY_NAME="rj-flask-client"
SUBSCRIPTION_ID="965..00f8d0"


# Docker Image
Push to ACR:

	docker build -t rj-client:v1 .

	docker tag rj-client:v1 rjsimpleflask.azurecr.io/rj-flask-client:v1

	docker push rjsimpleflask.azurecr.io/rj-flask-client:v1

az login
az acr login --name $ACR_BASE

# how to create a container app
az containerapp up \
	  --name $CONTAINERAPPS_NAME \
	  --resource-group $RESOURCE_GROUP \
	  --location $LOCATION \
	  --environment $CONTAINERAPPS_ENVIRONMENT \
	  --image $ACR_BASE.azurecr.io/$REPOSITORY_NAME:v1 \
	  --target-port 5001 \
	  --ingress external \
	  --query properties.configuration.ingress.fqdn \
	  --env-vars API_BASE=https://rj-server.wittyfield-91da3b68.centralindia.azurecontainerapps.io/


	# verify
	az containerapp logs show -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP --type system --tail 50

	az containerapp show -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP


# Update replicas
az containerapp update \
	--name $CONTAINERAPPS_NAME \
	--resource-group $RESOURCE_GROUP \
	--min-replicas 1 \
	--max-replicas 4

	# It is creating a new revision


# Check revision
az containerapp revision list \
  --name $CONTAINERAPPS_NAME \
  --resource-group $RESOURCE_GROUP \
  -o table



# rbac
az ad sp create-for-rbac \
  --name $CONTAINERAPPS_NAME \
  --role contributor \
  --scopes /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP \
  --json-auth \
  --output json



# Adding Label to the recent revision
az containerapp revision label add -n $CONTAINERAPPS_NAME -g $RESOURCE_GROUP --label v2 --revision latest

# Adding Label to the previous revision matching by revision (name)
az containerapp revision label add -g $RESOURCE_GROUP --label v1 --revision rj-client--gx7kp53

# Change revision mode
az containerapp revision set-mode \
  --name $CONTAINERAPPS_NAME \
  --resource-group $RESOURCE_GROUP \
  --mode multiple

# Split traffic
az containerapp ingress traffic set \
    --name $CONTAINERAPPS_NAME \
    --resource-group $RESOURCE_GROUP \
    --label-weight v1=80 v2=20


# Split traffic by version name
az containerapp ingress traffic set \
	-n $CONTAINERAPPS_NAME \
	-g $RESOURCE_GROUP \
	--revision-weight latest=20 cner-server--wg241rj=80
```


### Ref:
* [https://medium.com/@bassonrichard/github-actions-azure-container-apps-build-deploy-f15cb1dfbaa3](https://medium.com/@bassonrichard/github-actions-azure-container-apps-build-deploy-f15cb1dfbaa3)

* [https://dev.to/pwd9000/run-docker-based-github-runner-containers-on-azure-container-apps-aca-1n13](https://dev.to/pwd9000/run-docker-based-github-runner-containers-on-azure-container-apps-aca-1n13)



### Auto Deployment with ACA
```
https://github.com/kactlabs/titanic-prediction-flask

docker login --username=rajacsp

resource group:
ml-poc-riversand


Server:
	container-app-name:
		sample-flask-titanic-ml-server

	https://sample-flask-titanic-ml-server.victoriousmushroom-7878b821.centralindia.azurecontainerapps.io


v1:
	Decision Tree

	docker build -t ml-server .
	docker run -p 9090:5000 --name ml-server-112 ml-server:latest

	http://0.0.0.0:9090/

	Push to DockerHub:

		docker build -t titanic-ml-server:v1 .

		docker tag titanic-ml-server:v1 rajacsp/titanic-ml-server:v1
			https://hub.docker.com/repository/docker/rajacsp/titanic-ml-server/tags?page=1&ordering=last_updated



		docker push rajacsp/titanic-ml-server:v1

v2:
	SVC

	docker build -t titanic-ml-server:v2 .
	docker run -p 9091:5000 --name titanic-ml-server-v2 titanic-ml-server:v2

		if already available, use this:
		docker rm <id>

	Push to DockerHub:

		docker build -t titanic-ml-server:v2 .

		docker tag titanic-ml-server:v2 rajacsp/titanic-ml-server:v2

		docker push rajacsp/titanic-ml-server:v2


	Push to ACR:

		mlpocriversand.azurecr.io

		docker tag titanic-ml-server:v2 mlpocriversand.azurecr.io/titanic-ml-server:v2

		docker push mlpocriversand.azurecr.io/titanic-ml-server:v2

		5000



v3:
	LR


	docker build -t titanic-ml-server:v3 .
	docker run -p 9091:5000 --name titanic-ml-server-v3 titanic-ml-server:v3

		if already available, use this:
		docker rm <id>

	Push to DockerHub:

		docker build -t titanic-ml-server:v3 .

		docker tag titanic-ml-server:v3 rajacsp/titanic-ml-server:v3

		docker push rajacsp/titanic-ml-server:v3


	Push to ACR:

		mlpocriversand.azurecr.io

		docker tag titanic-ml-server:v3 mlpocriversand.azurecr.io/titanic-ml-server:v3

		docker push mlpocriversand.azurecr.io/titanic-ml-server:v2

		5000


Failed to deploy new revision: WorkloadProfiles configuration is not supported in  api version. Use 2022-11-01-preview or above.


az acr login --name mlpocriversand

# Create
az containerapp up \
  --name sample-flask-titanic-ml-server \
  --resource-group ml-poc-riversand \
  --location centralindia \
  --environment 'ml-poc-riversand' \
  --image mlpocriversand.azurecr.io/titanic-ml-server:v2 \
  --target-port 5000 \
  --ingress external \
  --query properties.configuration.ingress.fqdn

	# Verify
		az containerapp show -n sample-flask-titanic-ml-server -g ml-poc-riversand

		az containerapp logs show -n sample-flask-titanic-ml-server -g ml-poc-riversand

		http://sample-flask-titanic-ml-server.victoriousmushroom-7878b821.centralindia.azurecontainerapps.io


# Login ACR
az acr login --name mlpocriversand



# Check revision
az containerapp revision list \
  --name sample-flask-titanic-ml-server-1 \
  --resource-group ml-poc-riversand \
  -o table


# Create a revision
az containerapp revision copy \
	--container-name sample-flask-titanic-ml-server-1 \
	-n sample-flask-titanic-ml-server-1 \
	--resource-group ml-poc-riversand \
	--image mlpocriversand.azurecr.io/titanic-ml-server:v2 \
	--max-replicas 6 \
	--min-replicas 1 \
	--revision-suffix v2 \
	--cpu 0.75 --memory 1.5Gi


	https://learn.microsoft.com/en-us/cli/azure/containerapp/revision?view=azure-cli-latest#az-containerapp-revision-copy


# Update label on previous revision
az containerapp revision label add \
	-n sample-flask-titanic-ml-server-1 \
	-g ml-poc-riversand \
	--label v2 \
	--revision latest


# Udpate Traffic on multiple labels
az containerapp ingress traffic set \
	-n sample-flask-titanic-ml-server-1 \
	-g ml-poc-riversand \
	--label-weight v1=80 v2=20


	https://learn.microsoft.com/en-us/cli/azure/containerapp/ingress/traffic?view=azure-cli-latest#az-containerapp-ingress-traffic-set


Github Actions:

template:
az ad sp create-for-rbac \
	--name my-app-credentials \
	--role contributor \
	--scopes /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/my-container-app-rg \
	--json-auth \
	--output json

# get subscription id
az account show --query id

	5de4727f-d9d6-4052-81e4-bb3781f6c961

	https://yourazurecoach.com/2020/07/14/get-subscription-id-with-azure-cli/

az ad sp create-for-rbac \
	--name ml-server-creds \
	--role contributor \
	--scopes /subscriptions/5de4727f-d9d6-4052-81e4-bb3781f6c961/resourceGroups/ml-poc-riversand \
	--json-auth \
	--output json

https://learn.microsoft.com/en-us/azure/container-apps/github-actions

```