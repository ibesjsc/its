/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package MainProg;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

/**
 *
 * @author Luzec
 */
public class CuttingDataByDay {
    public static void DataByDay(String filename) throws FileNotFoundException, IOException{
        String sHeader = "";
        
        FileReader fr = new FileReader(filename);
        BufferedReader br = new BufferedReader(fr);
        
        // Get List distinct date
        ArrayList<String> lstDate = new ArrayList<String>();
        String sCurrentLine = br.readLine(); // remove header
        sHeader = sCurrentLine;
	while ((sCurrentLine = br.readLine()) != null) {
		String [] arrDate = sCurrentLine.split(",");
                String date = arrDate[3];
                
                if(!lstDate.contains(date)){
                    lstDate.add(date);
                }
	}
        br.close();
        fr.close();    
        System.out.println(lstDate);
        
        // Cutting date data
        for(String sdate : lstDate){
            ArrayList<SpeedItem> lstSubData = new ArrayList<SpeedItem>();
            fr = new FileReader(filename);
            br = new BufferedReader(fr);
            sCurrentLine = br.readLine(); // remove header
            while ((sCurrentLine = br.readLine()) != null) {
                String [] arrDate = sCurrentLine.split(",");
                String date = arrDate[3];
                if(sdate.equals(date)){
                    lstSubData.add(new SpeedItem(sCurrentLine));
                }            
            }
            br.close();
            fr.close();
            Collections.sort(lstSubData);
            
            // Write data to file
            
            if(lstSubData.size() == 61){ // 20 to 80 is 61 frame
                FileWriter fw = new FileWriter("E:\\\\PhD-Research\\\\Data_Experiment\\\\Non_Cutting_Data\\\\DataByDate\\"+sdate);
                BufferedWriter bw = new BufferedWriter(fw);
                bw.write(sHeader);
                bw.newLine();

                for(SpeedItem item : lstSubData){
                     bw.write(item.rawToString());
                     bw.newLine();
                }
                bw.close();
                fw.close();   
            }
        }
        
    }
}
