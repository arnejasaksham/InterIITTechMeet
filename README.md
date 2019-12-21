##  Schlumberger Coding Hackathon
<img src="https://user-images.githubusercontent.com/19551774/71306931-31fc1400-240d-11ea-9f6d-1f277fb31bb7.jpeg">

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
For the given problem statement, we propose a scalable, affordable, portable, modular and end-to-end solution to mitigate the need of manual surveying to track the project's construction update. Our solution consists of following entities:

### For tracking of ongoing construction project
- An android app for contractor to send the project updates in a regular constant interval by clicking the geo-tagged photo. Whenever, the contractor uploads the image of completed work from a particular location, the GPS of his/her mobile phone records the coordinates and send it to the server and accordingly the project status is calculated on the basis of proposed length and constructed lenghth and same is updated and reflected to both contractor(on Android app) and Government(on web dashboard). A map with poygraph of both proposed road and constructed road is also showed at both platform for better user's experience.
- A calendar graph is also available to visualize the project status. 
- A webapp dashboard where the Governement can see the project status of various ongoing projects and other relevant details.
- A Twitter chatbot which regularly and automatically post tweets containg the images of the completed work and project status on the Govt's twitter handle. This may serve as a good public-relation opportunity for government to show the ongoing infrastructure development under their regime.

### For road maintenance by crowdsourcing info of damaged road
- An android app for general public using which anyone can click an image of damaged road and sent it to a centralized server. The app will automatically record the GPS Coordinates and send it to the server. We propose a real-time object detection model using [YOLO and OpenCV](https://github.com/jhasuman/potholes-detection) which then updates the database in real-time with the detected road damages. The app has also interface for the users to track the status of their submitted reports.
- For government admin, we have a localized server setup with a web dashboard where they can see the status of all submitted reports in a tabular format. They can assign any of the road damages report to certain contractor to repair it and update the fix status which the user as well as Govt admin can see in the app and web dashboard respectively.
- An email is triggered to the contractors at real time to notify them of the upcoming tasks.
- All the road damages can be quickly viewed in the map by the Govt admin.

### Gamification
- To reward the road damage submitter and encourage others to submit the reports, we plan to incetivize every authentic road damage report submission.
- We have created a virtual wallet in which certain amount will be credited whenever an user submit an authentic report. These credits can be redeemed to the user's FASTag wallet.
- FASTag is a device that employs Radio Frequency Identification (RFID) technology for making toll payments directly from the prepaid account linked to it. Since, the FASTag is mandatory on National Highways from January 15th, this incentivization of road damages info crowdsourcing will help in the popularization of FASTag also.
- We have also implemented leaderboard and levels where different users can compete on the basis of who submits more report.

<center>
<img src="https://user-images.githubusercontent.com/19551774/71308131-86f45600-241e-11ea-8b27-92ef931e5635.png">
</center>

## Future Plans
- Road Damage detection using smartphone's accelerometer sensor. Android application detects a pothole when a car is passed through a pothole and reports the location of that pothole to the Road Ministry. All the other users can also view the potholes on map and find safest routes.
- A Twitter crawler which can analyze mentions, likes, retweets etc. and reward the general public appropriately for being a good samaritan and spreading awareness.
- We plan to rank the builders' appropriately via a ranking system based on their previous performance.

<center>
<h1>Thank You</h1>
</center>
