
package com.example.ncs_client;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Set up the input

                // TODO convertire conn_port in intero
                connectClient(ip_address.getText().toString(), conn_port);


    }


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

    private void connectClient(String ip, int porta) {
        //Create a new client
        client = new ClientSocket(ip, porta);
        //Start the client connection in the background
        client.execute();

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        //getMenuInflater().inflate(R.menu.main, menu);
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
                client.sendMessage(("2#" + x + "#" + y + "#"));
                break;
        }

        return false;
    }

}
