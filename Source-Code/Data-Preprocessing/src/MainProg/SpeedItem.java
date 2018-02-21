/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package MainProg;

/**
 *
 * @author Luzec
 */
public class SpeedItem implements Comparable {
    
    //public static double thresholdSpeed = 2.0;
    
    public String segmentID;
    public int dayOfWeek;
    public int frame;
    public String date;
    public double speed;

    public SpeedItem(String segmentID, int dayOfWeek, int frame, String date, double speed) {
        this.segmentID = segmentID;
        this.dayOfWeek = dayOfWeek;
        this.frame = frame;
        this.date = date;
        this.speed = speed / 65.0;
        //if(speed < thresholdSpeed){
            ///System.out.println("date: " + date + " - frame: " + frame + " - speed: " + speed);
        //}
        //this.speed = Math.round(1000.0 * (speed / 65.0))/1000.0;
    }
    
    public SpeedItem(String formatString){
        String [] arr = formatString.split(",");
        this.segmentID = arr[0];
        this.dayOfWeek = Integer.parseInt(arr[4]);
        this.frame = Integer.parseInt(arr[1]);
        this.date = arr[3];
        this.speed = Double.parseDouble(arr[2]) / 65.0;
        //this.speed = Math.round(1000.0 * (Double.parseDouble(arr[2]) / 65.0))/1000.0;
        
        //if(Double.parseDouble(arr[2]) < thresholdSpeed){
            //System.out.println("date: " + date + " - frame: " + frame + " - speed: " + Double.parseDouble(arr[2]) + 
                //    " - normalize speed: " + this.speed);
        //}
    }
    
    @Override
    public String toString(){
        //double temday =  Math.round(1000.0 * dayOfWeek / 7.0) / 1000.0;
        //double temframe =  Math.round(1000.0 * frame / 95.0) / 1000.0;
        //return String.valueOf(temday)+","+String.valueOf(temframe)+","+String.valueOf(speed);
        return String.valueOf(dayOfWeek / 7.0)+","+String.valueOf(frame / 95.0)+","+String.valueOf(speed);
    }
    
    public String rawToString(){
        //double temday =  Math.round(1000.0 * dayOfWeek / 7.0) / 1000.0;
        //double temframe =  Math.round(1000.0 * frame / 95.0) / 1000.0;
        //return String.valueOf(temday)+","+String.valueOf(temframe)+","+String.valueOf(speed);
        return segmentID +","+String.valueOf(frame)+","+String.valueOf(speed*65.0)+","+date+","+String.valueOf(dayOfWeek);
    }
    
    @Override
    public int compareTo(Object o) {
        SpeedItem speed = (SpeedItem)o;
        return ((Integer)this.frame).compareTo(speed.frame);     
    }
}
