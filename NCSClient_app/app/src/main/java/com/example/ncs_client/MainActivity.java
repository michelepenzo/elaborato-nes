
package com.example.ncs_client;


import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GestureDetectorCompat;
import android.content.Context;
import android.os.Bundle;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.StrictMode;
import android.text.InputType;
import android.view.GestureDetector;
import android.view.Menu;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity implements GestureDetector.OnGestureListener, GestureDetector.OnDoubleTapListener{

    ClientSocket client;
    private static final String DEBUG_TAG = "Gestures";
    private GestureDetectorCompat mDetector;
    private int x;
    private int y;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mDetector = new GestureDetectorCompat(this,this);
        //mDetector.setOnDoubleTapListener(this);
        mDetector.setIsLongpressEnabled(true);



        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        /*
        Button btnLeft = (Button) findViewById(R.id.btn_leftClick);
        Button btnRight = (Button) findViewById(R.id.btn_rightClick);
         */

        //Display a pop-up requesting the target machine IP
        AlertDialog.Builder builder = new AlertDialog.Builder(this);

        Context context = builder.getContext();
        LinearLayout layout = new LinearLayout(context);
        layout.setOrientation(LinearLayout.VERTICAL);

        //builder.setTitle("Inserisci:");

        // Set up the input
        final EditText ip_input = new EditText(this);
        ip_input.setInputType(InputType.TYPE_CLASS_PHONE);
        ip_input.setHint("Inserisci indirizzo IP");
        layout.addView(ip_input);
        /*
        final EditText port_input = new EditText(this);
        port_input.setInputType(InputType.TYPE_CLASS_NUMBER);
        port_input.setHint("Porta");
        layout.addView(port_input);

        final EditText bound_input = new EditText(this);
        bound_input.setInputType(InputType.TYPE_CLASS_NUMBER);
        bound_input.setHint("Delay massimo (millisecondi)");
        layout.addView(bound_input);
        */
        builder.setView(layout);

        // Set up the buttons
        builder.setPositiveButton("Connetti", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                //Enter the IP to the client
                //connectClient(ip_input.getText().toString(), Integer.parseInt(port_input.getText().toString()), Integer.parseInt(bound_input.getText().toString()) );
                connectClient(ip_input.getText().toString(), 5050);
            }
        });

        builder.show();
        /*
        btnLeft.setOnClickListener(btnLeft_onClick);
        btnRight.setOnClickListener(btnRight_onClick);

         */

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);

        return true;
    }
    /*
    public OnClickListener btnLeft_onClick = new OnClickListener() {
        public void onClick(final View v) {
            client.sendMessage(("2#0#0#"));
        }
    };

    public OnClickListener btnRight_onClick = new OnClickListener() {
        public void onClick(final View v) {
            client.sendMessage(("3#0#0#"));
        }
    };

     */
    
    private void connectClient(String ip, int port){ //}, int bound) {
        //Create a new client

        /*
        if(bound > 1000)
            bound = 1000;
        */


        client = new ClientSocket(ip, port);//, bound);

        //Start the client connection in the background
        client.execute();
    }

    @Override
    public boolean onTouchEvent(MotionEvent event){


        if (this.mDetector.onTouchEvent(event) == true) {
            // questo  va bene per il movimento continuo
            x = (int)event.getX();
            y = (int)event.getY();


            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    client.sendMessage(("0#" + x + "#" + y + "#"));
                    break;
                case MotionEvent.ACTION_MOVE:
                    client.sendMessage(("1#" + x + "#" + y + "#"));
                    break;

                default:
                    break;
            }
        }
        else{
            // questo mi va bene per la pressione, come se fosse doppio tap
            x = (int)event.getX();
            y = (int)event.getY();

            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    client.sendMessage(("0#" + x + "#" + y + "#"));
                    break;
                case MotionEvent.ACTION_MOVE:
                    client.sendMessage(("1#" + x + "#" + y + "#"));
                    break;

                default:
                    break;
            }
        }
        return true;
    }

    @Override
    public boolean onDoubleTapEvent(MotionEvent event) {
        client.sendMessage(("4#0#0#"));
        return true;
    }

    @Override
    public void onLongPress(MotionEvent event) {
        client.sendMessage(("4#0#0#"));
    }

    // ---------------------------------------------------------------------------------------------

    @Override
    public boolean onDoubleTap(MotionEvent event) {
        return true;
    }

    @Override
    public boolean onDown(MotionEvent event) {
        return true;
    }

    @Override
    public boolean onFling(MotionEvent event1, MotionEvent event2,
                           float velocityX, float velocityY) {
        return true;
    }

    @Override
    public boolean onScroll(MotionEvent event1, MotionEvent event2, float distanceX,
                            float distanceY) {
        return true;
    }

    @Override
    public void onShowPress(MotionEvent event) {
    }

    @Override
    public boolean onSingleTapUp(MotionEvent event) {
        return true;
    }

    @Override
    public boolean onSingleTapConfirmed(MotionEvent event) {
        return true;
    }

}

