import java.io.*;
import java.net.*;
import java.util.Date;
 
/**
 * This program demonstrates a simple TCP/IP socket server.
 *
 * @author www.codejava.net
 */
public class TimeServer {
 
    public static void main(String[] args) {

        try (ServerSocket serverSocket = new ServerSocket(0)) {
 
            System.out.println("PORT " + serverSocket.getLocalPort());



                Socket socket = serverSocket.accept();

                System.out.println("New client connected");



            while (true) {
                //System.out.println("-----------------------------------------------------------------------------");
                OutputStream output = socket.getOutputStream();
                //System.out.println("-----------------------------------------------------------------------------");
                PrintWriter writer = new PrintWriter(output, true);
                
                writer.println(new Date().toString());
            }
 
        } catch (IOException ex) {
            System.out.println("Server exception: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

}