//<script src="https://www.gstatic.com/firebasejs/5.9.2/firebase.js"></script>
//<script src="https://www.gstatic.com/firebasejs/5.9.2/firebase-app.js"></script>

var config = {
    apiKey: "AIzaSyA1njsn06UVdJUBzU4nOCaNRUPbZLUInic",
    authDomain: "hackathon-74ece.firebaseio.com",
    databaseURL: "https://hackathon-74ece.firebaseio.com/",
    projectId: "hackathon-74ece",
    storageBucket: "hackathon-74ece.appspot.com",
    messagingSenderId: "1024313734913"
  };
//firebase.initializeApp(config);

var mainApp=firebase.initializeApp(config);
console.log(mainApp.name);
var fireDatabase=firebase.database();

//code sample for read
/*
fireDatabase.ref("Pothole_Reports/dAvBxyWOA8ehDQGPVR9ONWtsSb23/20190330_153031/").child("Status").on('value', function(snapshot){
	console.log(snapshot.val());
});
*/
//code sample for update
statusData={"Status":60};
fireDatabase.ref("Pothole_Reports/Pothole_Reports/8hmEFVWmwVf6bIsbsg64ap7ZNaH2/20191220_122311/").update(statusData);