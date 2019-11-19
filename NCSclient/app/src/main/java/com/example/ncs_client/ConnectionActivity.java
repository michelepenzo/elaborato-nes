package com.example.ncs_client;


public class ConnectionActivity extends AppCompatActivity {

    ClientSocket client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_connection);

        Button btn_connect = (Button) findViewById(R.id.btn_connect);
        final EditText ip_address = (EditText) findViewById(R.id.address);  // indirizzo ip
        final EditText conn_port = (EditText) findViewById(R.id.port);            // porta di connessione


        btn_connect.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                // Set up the input

                // TODO convertire conn_port in intero
                connectClient(ip_address.getText().toString(), conn_port);

                Intent intent = new Intent(v.getContext(), MainActivity.class);
                v.getContext().startActivity( intent );
            }
        });


    }

}