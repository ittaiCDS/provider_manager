# PM
Provider Manager

--- 

## PM Manual


### Installation

###### On your system:
1. Install Python 3.1X
2. Install Git
3. Install Postgresql
4. Clone this project
5. Install angular cli v 12
```
npm install -g @angular/cli@12
```
6. go to /admin and install Node Modules
```
npm install
```
7. Create a virtual environment "env" into root project folder (Must be Python 3.10) and activate this:
```
virtualenv -p python3.1X env
source env/bin/activate
```

8. Python additional dev services may be needed, run:
```


```
9. Install Requirements under api/ folder with (env started) 
 ```
pip install -r requirements.txt
```
10. Run django server
```
./run-backend.sh
```
    
At this point you should be able to run the proyect following the usage instructions

---------

### Usage


##### DB Local Connection


##### Frontend


##### Backend

1. Activate virtual environment:
```
source env/bin/activate
```

2. Within proyect folder run:
```
./run-backend.sh
```

-----

### Deployment

#### Full Deploy:

1. Activate your virtual environment
2. Incorporate changes from a git branch into your current local branch:
```
git pull
```
2. Run the following command
```

```


At this point a long time deployment will start. If there is an error it will stop.

#### Backend only deploy:

###### If your static folder doesn't contain Angular Dist prod build this deploy will broke the system

1. Activate your virtual environment
2. Incorporate changes from a git branch into your current local branch:
```
git pull
```
3. Go to apiserver/ folder:
```
cd apiserver/
```
4. Run single command:
```

```

---

### Sites

Developer site: https://morfeo-dev-321917.appspot.com/admin/login

Production site: https://morfeo-prod.appspot.com/admin/login

---

Last revised: March 2024
By: CDS - Marco Hernandez
Done in Windows 10

