package com;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Created by bzhang345 on 4/18/18.
 */
public class HomescreenAdmin {
    private JPanel panel1;
    private JLabel welcomeLabel;
    private JButton logoutButton;
    private JButton viewPendingAnimalsAndCropsButton;
    private JButton viewApprovedAnimalsAndCropsButton;
    private JButton viewUnconfirmedPropertiesButton;
    private JButton viewConfirmedPropertiesButton;
    private JButton viewOwnersListButton;
    private JButton viewVisitorListButton;

    public HomescreenAdmin(JFrame frame) {


        welcomeLabel.setText("Welcome Bryan!");
        viewVisitorListButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                JFrame frame1 = new JFrame("App");
                frame1.setSize(1000, 700);
                frame1.setContentPane(new App().panel1);
                frame1.setVisible(true);
                frame.setVisible(false);
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("HomescreenAdmin");
        frame.setSize(1000, 700);
        frame.setContentPane(new HomescreenAdmin(frame).panel1);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
      //  HomescreenAdmin homescreen = new HomescreenAdmin(frame);

        //JFrame frame2 = new JFrame("App");


    }
}
