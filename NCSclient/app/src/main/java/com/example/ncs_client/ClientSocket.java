package com.example.ncs_client;

import java.net.*;
import java.io.*;

import android.os.AsyncTask;
import android.os.StrictMode;
import java.util.Random;



public class ClientSocket extends AsyncTask<String, Void, String> {
    private Socket socket = null;
    private OutputStream streamOut = null;
    private String serverName;
    private int serverPort;
    private boolean connected = false;
    private Random rand = new Random();
    private int boundDelay;
    private int minBound ;


    public ClientSocket(String server, int port)//, int bound)
    {
        serverName = server;
        serverPort = port;
        // boundDelay = bound;
    }

    public void sendMessage(String msg) throws NullPointerException{

        if(connected) {
            try
            {
                byte[] msgBytes = msg.getBytes();

                /*
                NO DELAY ON SERVER
                try {
                    Thread.sleep( rand.nextInt(boundDelay) );
                }
                catch(InterruptedException e) {}
                */
                streamOut.write(msgBytes);
                streamOut.flush();
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