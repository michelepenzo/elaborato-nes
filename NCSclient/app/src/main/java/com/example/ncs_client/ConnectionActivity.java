package com.example.ncs_client;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class ConnectionActivity extends AppCompatActivity {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_connection);

        Button btn_connect = (Button) findViewById(R.id.btn_connect);


        btn_connect.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                // TODO connessione TCP



                Intent intent = new Intent(v.getContext(), MainActivity.class);
                v.getContext().startActivity( intent );
            }
        });


    }
}