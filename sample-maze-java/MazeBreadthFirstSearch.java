import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import java.awt.event.*;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import Maze1.*;
/**
 * Title: MazeBreadthFirstSearch
 * <p>
 * Description: Demo program for Java AI Programming
 * <p>
 * Copyright: Copyright (c) Mark Watson, Released under Open Source Artistic
 * License
 * <p>
 * Company: Mark Watson Associates
 * <p>
 * 
 * @author Mark Watson
 * @version 1.0
 */

public class MazeBreadthFirstSearch extends javax.swing.JFrame {
	JPanel jPanel1 = new JPanel();
	Maze currentSearchEngine = null;

	BufferedImage[] images; // contain images

	public MazeBreadthFirstSearch() {
		try {
			jbInit();
			loadimages(); // load images in array
		} catch (Exception e) {
			System.out.println("GUI initilization error: " + e);
		}
		currentSearchEngine = new Maze(10, 10);
		repaint();
	}

	public void paint(Graphics g_unused) {
		if (currentSearchEngine == null)
			return;
		//Maze maze = currentSearchEngine.getValue();
		int width = currentSearchEngine.getWidth();
		int height = currentSearchEngine.getHeight();
		System.out.println("Size of current maze: " + width + " by " + height);
		Graphics g = jPanel1.getGraphics();
		Graphics g2 = jPanel1.getGraphics();
		g2.setColor(Color.white);
		g2.fillRect(0, 0, 320, 320);
		g2.setColor(Color.black);
		currentSearchEngine.setValue(0, 0, Maze.START_LOC_VALUE);
		for (int x = 0; x < width; x++) {
			for (int y = 0; y < height; y++) {
				short val = currentSearchEngine.getValue(x, y);

				if (val == Maze.OBSTICLE) {
					g2.drawImage(images[0], 6 + x * 29, 3 + y * 29, null);

				} else if (val == Maze.START_LOC_VALUE) {
					g2.drawImage(images[1], 6 + x * 29, 3 + y * 29, null);

				} else if (val == Maze.GOAL_LOC_VALUE) {
					g2.drawImage(images[2], 6 + x * 29, 3 + y * 29, null);

				} else {

					g2.setColor(Color.GREEN);
					g2.fillRect(6 + x * 29, 3 + y * 29, 29, 29);
					g2.setColor(Color.BLUE);
					g2.drawRect(6 + x * 29, 3 + y * 29, 29, 29);
				}
			}
		}
		// redraw the path in black:
		g2.setColor(Color.black);
		/*Dimension[] path = Maze.getPath();
		for (int i = 1; i < (path.length - 1); i++) {
			int x = path[i].width;
			int y = path[i].height;
			short val = currentSearchEngine.getValue(x, y);
			g2.drawString("" + (path.length - i), 16 + x * 29, 19 + y * 29);
		}*/

	}

	

	private void loadimages() {
		try {

			images = new BufferedImage[4];
			images[0] = ImageIO.read(new File("images/brick.png"));
			images[1] = ImageIO.read(new File("images/monster.png"));
			images[2] = ImageIO.read(new File("images/pacman.png"));

		} catch (IOException ex) {
			Logger.getLogger(MazeBreadthFirstSearch.class.getName()).log(Level.SEVERE, null, ex);
		}
	}

	private void jbInit() throws Exception {

		this.setContentPane(jPanel1);
		this.setCursor(null);
		this.setDefaultCloseOperation(3);
		this.setTitle("MazeBreadthFirstSearch");
		this.getContentPane().setLayout(null);
		jPanel1.setBackground(Color.white);
		jPanel1.setDebugGraphicsOptions(DebugGraphics.NONE_OPTION);
		jPanel1.setDoubleBuffered(false);
		jPanel1.setRequestFocusEnabled(false);
		jPanel1.setLayout(null);
		this.setSize(320, 340);
		this.setVisible(true);
	}

	public static void main(String[] args) {
		MazeBreadthFirstSearch mazeSearch1 = new MazeBreadthFirstSearch();
	}
}