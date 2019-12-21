package c.example.communityreport;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class RewardsActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.points);

        TextView level_view = (TextView) findViewById(R.id.textView4);
        int level = (int) Math.ceil(Math.log10(1+1));  //TODO: fetch points
        level_view.setText("You are at Level " + level);

        TextView credits_view = (TextView) findViewById(R.id.textView5);
        int credits;  //TODO: fetch remaining credits
        credits_view.setText("Remaining Credits: \\u20B9 " + 5);


    }

    public void setZero(View view)
    {
        ((TextView)findViewById(R.id.textView5)).setText("Remaining Credits: \\u20B9 0)");
    }
}