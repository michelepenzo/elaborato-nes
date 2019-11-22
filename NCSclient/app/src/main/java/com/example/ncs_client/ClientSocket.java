package com.example.ncs_client;

import java.net.*;
import java.io.*;

import android.os.AsyncTask;

public class ClientSocket extends AsyncTask<String, Void, String> {
    private Socket socket = null;
    private OutputStream streamOut = null; // TODO far combaciare i tipi di java con il server
    private String serverName;
    private int serverPort;
    private boolean connected = false;

    public ClientSocket(String server, int port)
    {
        serverName = server;
        serverPort = port;
    }

    public void sendMessage(String msg) throws NullPointerException{

        if(connected) {
            try
            {
                //Convert the string into a byte array for C# to read
                byte[] msgBytes = msg.getBytes();
                System.out.println("-----------------------------------------------------------------------------");
                //Send off the message
                streamOut.write(msgBytes);
                System.out.println("-----------------------------------------------------------------------------");
                streamOut.flush();
                System.out.println("-----------------------------------------------------------------------------");
            }
            catch(IOException ioe) {
                System.out.println("Sending error: " + ioe.getMessage());
            }
        }

    }

    private void start() throws IOException
    {
        streamOut = new DataOutputStream(socket.getOutputStream());

    }

    public void stop() {
        //Stop the socket and output streams
        try {
            if (streamOut != null)  streamOut.close();
            if (socket    != null)  socket.close();
            connected= false;
        }
        catch(IOException ioe) {
            System.out.println("Error closing ...");
        }
    }

    @Override
    protected String doInBackground(String... params) {
        System.out.println("Establishing connection to server. Please wait ...");

        try {
            System.out.println("Attempting to connect to " + serverName + ":" + serverPort);
            socket = new Socket(serverName, serverPort);
            System.out.println("Connected: " + socket);
            connected = true;
            start();
        }
        catch(UnknownHostException uhe) {
            System.out.println("Host unknown: " + uhe.getMessage());
        }
        catch(IOException ioe) {
            System.out.println("Unexpected IO exception: " + ioe.getMessage());
        }
        catch(Exception fe) {
            System.out.println("Unexpected fatal exception: " + fe);
        }


        return null;
    }
}