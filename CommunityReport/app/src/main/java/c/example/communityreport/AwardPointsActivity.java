package c.example.communityreport;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Map;

public class AwardPointsActivity extends AppCompatActivity{

    //Firebase vairables
    FirebaseAuth firebaseAuth;
    StorageReference storageReference;
    DatabaseReference databaseReference;
    FirebaseUser firebaseUser;
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_awardpoints);
        //Log.e("A","B");
        //Toast.makeText(this,"A",Toast.LENGTH_LONG).show();
        tv = findViewById(R.id.textView);
        final TextView tv2 = findViewById(R.id.textView4);

        firebaseAuth = FirebaseAuth.getInstance();
        databaseReference = FirebaseDatabase.getInstance().getReference();
        firebaseUser = firebaseAuth.getCurrentUser();
        storageReference = FirebaseStorage.getInstance().getReference();
        StringBuilder content = new StringBuilder();
        //new getData().execute("https://hackathon-74ece.firebaseio.com/Pothole_Reports.json");
        final List<Integer> im = new ArrayList<>();
        databaseReference.child("Pothole_Reports").child(firebaseUser.getUid()).addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {

                for (DataSnapshot dataSnapshot : snapshot.getChildren()) {
                    ImageInformation imageInformation = dataSnapshot.getValue(ImageInformation.class);
                    if(imageInformation.accepted)
                        im.add(1);
                    /*for(int i=0; i<imageInformation.im.size();i++)
                    if (imageInformation.DownloadUrl!=null && imageInformation.DownloadUrl.length() >= 50)
                    {
                        int val = Integer.parseInt(tv.getText().toString());
                        tv.setText((val+20)+"");
                    }*/
                }
                tv2.setText((im.size()*20)+"");
                Toast.makeText(AwardPointsActivity.this,"Congrats. Your points are "+im.size()*20, Toast.LENGTH_LONG).show();
            }
            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });



    }

    private class getData extends AsyncTask<String, Integer, String> {
        protected String doInBackground(String... urls) {
            String stringUrl = urls[0];
            StringBuilder content = null;
            URL url = null;
            try {
                    url = new URL(stringUrl);
                    URLConnection urlConnection = url.openConnection();
                    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                    String line;
                    while ((line = bufferedReader.readLine()) != null)
                    {
                        content.append(line + "\n");
                    }
                    bufferedReader.close();
                } catch (Exception e) {
                e.printStackTrace();
            }
            Log.e("Umm",content.toString());
            return content.toString();
        }

        protected void onProgressUpdate(Integer... progress) {
            //setProgressPercent(progress[0]);
        }

        protected void onPostExecute(String result) {
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            String s = "";
            ListImageInfo imageInformation = gson.fromJson(result,ListImageInfo.class);
            for (ImageInformation imageinformation: imageInformation.im){
                s+=imageinformation.DownloadUrl+",";
            }
            tv.setText(s);
        }
    }

    class ListImageInfo
    {
        ArrayList<ImageInformation> im;
        ListImageInfo()
        {
            im = new ArrayList<>();
        }
    }
}
