<div align="center"> <h1>Schlumberger Coding Hackathon</h1> </div>
<p align="center">
<img src="https://user-images.githubusercontent.com/19551774/71306931-31fc1400-240d-11ea-9f6d-1f277fb31bb7.jpeg">
</p>

**Problem Statement**: [Roads’ Leasing and Maintenance](http://www.interiittech.org/events/hackathon.html)
-  When Government leases roads to contractors, it has no way of checking the progress of the project and has to rely on manual surveys and what not.
    
-  Further, maintenance of the leased road is a huge pain. The government must perform regular surveys to check whether the road is in good condition.
    
-  Can you design a system where this process can be simplified or gamified by which we can crowd source this kind of data?
    
-  Make sure that a user who provides data can track the reported finding till it is resolved.
    
-  The system should be portable device friendly.

**Team**: [IIT Bhubaneswar](http://www.iitbbs.ac.in)

**Team Members**
- [Aditya Pal](https://www.github.com/PalAditya)
- [Aman Pratap Singh](https://www.github.com/apsknight)
- [Saksham Arneja](https://www.github.com/ArnejaSaksham)
- [Tummala Madhav](https://www.github.com/MadhavChoudhary)

## Abstract
For the given problem statement, we propose a scalable, affordable, portable, modular and end-to-end solution to mitigate the need of manual surveying to track the project's construction update. We named it **SwayamSevak**.

<p align="center">
<img src="https://user-images.githubusercontent.com/29799995/71309714-4baf5280-2431-11ea-96c0-00a3df8e884c.png">
</p>

The **android app** and **web app** together provide features for the following entities:

### For tracking of ongoing construction project
- An android app for contractor to send the project updates in a regular constant interval by clicking the geo-tagged photo. Whenever, the contractor uploads the image of completed work from a particular location, the GPS of his/her mobile phone records the coordinates and send it to the server and accordingly the project status is calculated on the basis of proposed length and constructed lenghth and same is updated and reflected to both contractor(on Android app) and Government(on web dashboard). A map with poygraph of both proposed road and constructed road is also showed at both platform for better user's experience.

<p align="center">
<img width="20%" height="20%" src="https://user-images.githubusercontent.com/29799995/71308924-fae72c00-2427-11ea-90fc-c2a56078e34f.jpg">
<img width="60%" height="60%" src="https://user-images.githubusercontent.com/29799995/71309606-ec047780-242f-11ea-858e-a34e14d44a92.png">   
</p>

- A calendar graph is also available to visualize the project status. 

<p align="center">
<img width="80%" height="80%" src="https://user-images.githubusercontent.com/29799995/71308832-2cabc300-2427-11ea-9bad-8ba0f05843a8.png">
</p>

- A webapp dashboard where the Governement can see the project status of various ongoing projects and other relevant details.

<p align="center">
<img width="80%" height="80%" src="https://user-images.githubusercontent.com/29799995/71308813-0be36d80-2427-11ea-98c9-90dcc7e04fda.png">
</p>

<p align="center">
<img width="80%" height="80%" src="https://user-images.githubusercontent.com/29799995/71308812-09811380-2427-11ea-956c-9247f61f2328.png">
</p>

- A Twitter chatbot which regularly and automatically post tweets containg the images of the completed work and project status on the Govt's twitter handle. This may serve as a good public-relation opportunity for government to show the ongoing infrastructure development under their regime.

<p align="center">
<img width="80%" height="80%" src="https://user-images.githubusercontent.com/19551774/71310008-c62da180-2434-11ea-9404-6b709ee932e1.png">
</p>

### For road maintenance by crowdsourcing info of damaged road
- An android app for general public using which anyone can click an image of damaged road and sent it to a centralized server. The app will automatically record the GPS Coordinates and send it to the server. We propose a real-time object detection model using [YOLO and OpenCV](https://github.com/jhasuman/potholes-detection) which then updates the database in real-time with the detected road damages. The app has also interface for the users to track the status of their submitted reports.

<p align="center">
<img width="20%" height="20%" src="https://user-images.githubusercontent.com/29799995/71308918-f15dc400-2427-11ea-943f-ae754fd93522.jpg">   
<img width="20%" height="20%" src="https://user-images.githubusercontent.com/29799995/71308915-e30fa800-2427-11ea-80bc-112a4463c7aa.jpg">
<img width="20%" height="20%" src="https://user-images.githubusercontent.com/29799995/71308916-e5720200-2427-11ea-8463-51057cf277c4.jpg">
<img width="20%" height="20%" src="https://user-images.githubusercontent.com/29799995/71308922-f884d200-2427-11ea-854d-10c34b282b89.jpg">    
</p>

- For government admin, we have a localized server setup with a web dashboard where they can see the status of all submitted reports in a tabular format. They can assign any of the road damages report to certain contractor to repair it and update the fix status which the user as well as Govt admin can see in the app and web dashboard respectively.

<p align="center">
<img width="80%" height="80%" src="https://user-images.githubusercontent.com/29799995/71308816-11d94e80-2427-11ea-9fb9-eddab65a861e.png">
<img width="80%" height="80%" src="https://user-images.githubusercontent.com/29799995/71308815-0ede5e00-2427-11ea-9040-1e08641cae9a.png">  
</p>

- All the road damages can be quickly viewed in the map by the Govt admin.

<p align="center">
<img width="80%" height="80%" src="https://user-images.githubusercontent.com/29799995/71308822-1f8ed400-2427-11ea-9ab0-c7b68f68b8d9.png">
</p>

- An email is triggered to the contractors to notify them of the upcoming tasks and repairs. Report is generated upon fixing or completiong of a project.

<p align="center">
<img width="60%" height="60%" src="https://user-images.githubusercontent.com/29799995/71309992-86ff5080-2434-11ea-85af-489890e927e8.png">
</p>


### Gamification
- To reward the road damage submitter and encourage others to submit the reports, we plan to incetivize every authentic road damage report submission.
- We have created a virtual wallet in which certain amount will be credited whenever an user submit an authentic report. These credits can be redeemed to the user's FASTag wallet.
- FASTag is a device that employs Radio Frequency Identification (RFID) technology for making toll payments directly from the prepaid account linked to it. Since, the FASTag is mandatory on National Highways from January 15th, this incentivization of road damages info crowdsourcing will help in the popularization of FASTag also.
- We have also implemented leaderboard and levels where users are ranked on the basis of their activeness in reporting damages and problems or correcting the status of the project.

<p align="center">
<img width="40%" height="40%" src="https://user-images.githubusercontent.com/19551774/71308131-86f45600-241e-11ea-8b27-92ef931e5635.png">
<img width="40%" height="40%" src="https://user-images.githubusercontent.com/29799995/71310019-fe34e480-2434-11ea-920d-4018672a3187.jpg">
</p>

## Future Plans
- Road Damage detection using smartphone's accelerometer sensor. Android application detects a pothole when a car is passed through a pothole and reports the location of that pothole to the Road Ministry. All the other users can also view the potholes on map and find safest routes.
- A Twitter crawler which can analyze mentions, likes, retweets etc. and reward the general public appropriately for being a good samaritan and spreading awareness.
- We plan to rank the builders' appropriately via a ranking system based on their previous performance.

<center>
<h1>Thank You</h1>
</center>
