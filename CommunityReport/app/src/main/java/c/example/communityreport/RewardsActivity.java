package c.example.communityreport;

import android.app.Activity;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;

import java.util.ArrayList;
import java.util.List;

public class RewardsActivity extends AppCompatActivity {

    FirebaseAuth firebaseAuth;
    StorageReference storageReference;
    DatabaseReference databaseReference;
    FirebaseUser firebaseUser;
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.points);
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
                im.clear();
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
                int points = im.size()*10;
                int level = (int)Math.ceil(Math.log10(points + 2));  //TODO: fetch point
                tv2.setText("You are at level "+level+" with "+points+" points");
                Toast.makeText(RewardsActivity.this,"Congrats. Your points are "+im.size()*10, Toast.LENGTH_LONG).show();
            }
            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });


        TextView credits_view = findViewById(R.id.textView5);
        int credits;  //TODO: fetch remaining credits
        credits_view.setText("Remaining Credits: Rs. " + "50");


    }

    public void setZero(View view)
    {
        TextView textView = findViewById(R.id.textView5);
        textView.setText("Remaining Credits: Rs. 0");
    }
}