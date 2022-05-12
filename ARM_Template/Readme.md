# Deploy Azure Resource Management Template for creating the infrastructure of this pipeline.

## To run this deployment command, you must have the latest version of Azure CLI.


	templateFile="{path-to-the-template-file}"
	devParameterFile="{path-to-azuredeploy.parameters.dev.json}"
	az group create \
  		--name myResourceGroupDev \
  		--location "Germany West Central"
	az deployment group create \
  		--name devenvironment \
 		--resource-group myResourceGroupDev \
  		--template-file $templateFile \
  		--parameters $devParameterFile
