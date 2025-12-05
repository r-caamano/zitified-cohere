## zitified-cohere

`zitified-cohere` provides an example of zitifying the Cohere API Python SDK to encapsulate Cohere chat API
calls over a NetFoundry Zero Trust Overlay.

## Setup and Configure the Example

![Diagram](network.png)

Create or use an existing ziti network with at least one NF hosted edge router. This can be accomplished using the NetFoundry
Console.


1. Create an ubuntu 22.04 vm in AWS or other location with internet access
   a. install prereqs 

      ```sudo apt update```

      ```sudo apt upgrade```

      ```sudo apt install python3-pip python3-venv git```
      
   b. ## Build the Example
      On the linux system that will run the Client
      clone the repo
      mkdir ~/repos
      cd ~/repos
      ```git clone https://github.com/r-caamano/zitified-cohere.git```
      cd zitified-cohere/src

2. Create and enroll a ziti identity place the identity json file in the ~/repos/zitified-cohere/src on the VM created in step 1.
   ```
   a. cohere_client01
   ```

2. Add a Customer hosted edge router "gcp-cohere-edge01" to your network

![Diagram](add_router.png)

4. Launch the customer hosted edge-router in GCP follow https://console.cloud.google.com/marketplace/product/netfoundry/netfoundry-edge-router
 

3. Create a NF service named "cohere_api_service" and use address "api.cohere.com" , protocol TCP and 443 as the
   port. Assign the router identity e.g. gcp-cohere-edge01 as the hosting entity and forward address, protocol and port to yes.

![Diagram](service.png)

5. Create a service policy to bind the identity to the NF service e.g.

![Diagram](service-policy.png)

6. Create a router policy and with the NF hosted edge-router and the cohere_client as the identity e.g.

![Diagram](router-policy.png)



4. On the VM created in step one sent a chat command via using zcohere.py e.g.

   a. Create a python virtual environment

      ```cd ~/repos/zitified-cohere/src```

      ```python3 -m venv cohere```

      ```source cohere/bin/activate```

   b. install openziti and cohere modules
      ```pip3 install openziti```
      ```pip3 install cohere``` 

   c. execute script ```python zcohere.py --api-key <"your cohere api key"> --ziti-identity <identity json file> --message "Write a haiku about trees" ```
   

   Sample output:

   ```
   Whispering giants,  
   Roots deep in earth, leaves in sky,  
   Life’s silent pillars.

   ```