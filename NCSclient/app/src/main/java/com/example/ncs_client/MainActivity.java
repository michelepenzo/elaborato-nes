
package com.example.ncs_client;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.StrictMode;
import android.text.InputType;
import android.view.Menu;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity {

    ClientSocket client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

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

        builder.setTitle("Inserisci i valori di:");

        // Set up the input
        final EditText ip_input = new EditText(this);
        ip_input.setInputType(InputType.TYPE_CLASS_PHONE);
        ip_input.setHint("Indirizzo IP");
        layout.addView(ip_input);

        final EditText port_input = new EditText(this);
        port_input.setInputType(InputType.TYPE_CLASS_NUMBER);
        port_input.setHint("Porta");
        layout.addView(port_input);

        builder.setView(layout);

        // Set up the buttons
        builder.setPositiveButton("Connetti", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                //Enter the IP to the client
                connectClient(ip_input.getText().toString(), Integer.parseInt(port_input.getText().toString()));
            }
        });

        builder.show();
/*
        btnLeft.setOnClickListener(btnLeft_onClick);
        btnRight.setOnClickListener(btnRight_onClick);


 */
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
    private void connectClient(String ip, int port) {
        //Create a new client
        //ip="192.168.1.9";
        client = new ClientSocket(ip, port);
        //Start the client connection in the background
        client.execute();

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);

        return true;
    }



    public boolean onTouchEvent(MotionEvent event) {
        int x = (int)event.getX();
        int y = (int)event.getY();
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                client.sendMessage(("0#" + x + "#" + y + "#"));
                break;
            case MotionEvent.ACTION_MOVE:
                client.sendMessage(("1#" + x + "#" + y + "#"));
                break;
            case MotionEvent.ACTION_UP:
                //client.sendMessage(("2#" + x + "#" + y + "#"));
                break;
        }

    return false;
    }

}

