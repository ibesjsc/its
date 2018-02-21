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
public class Case3 {
    public static int LOOK_BACK = 1; // time_step
    // Xét feature Framely
    public static void ProcessingDataTimeStep_k_Feature_2(String inFileName, String outFileName) throws FileNotFoundException, IOException{
        FileReader fr = new FileReader(inFileName);
        BufferedReader br = new BufferedReader(fr);
        
        // Get List distinct date
        ArrayList<String> lstDate = new ArrayList<String>();
        String sCurrentLine = br.readLine(); // remove header
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
        
        // Tạo mảng lưu trữ các listSub
        ArrayList<SingleListSpeed> listSingle = new ArrayList<SingleListSpeed>();
        /// Xử lý từng ngày
        for (String _d : lstDate){
            SingleListSpeed obj = new SingleListSpeed(_d);
            fr = new FileReader(inFileName);
            br = new BufferedReader(fr);     
        // Get List distinct date
            sCurrentLine = br.readLine(); // remove header
            while ((sCurrentLine = br.readLine()) != null) {
                    SpeedItem itemSp = new SpeedItem(sCurrentLine);
                    if(itemSp.date.equals(_d)){
                        obj.lstSpeed.add(itemSp);
                    }
            }
            Collections.sort(obj.lstSpeed);
            listSingle.add(obj);
        }
        
        br.close();
        fr.close();   
        System.out.println(listSingle.size());
        
        
        ArrayList<ArrayList<String>> dataLookBack =  new ArrayList<ArrayList<String>>();
        for(SingleListSpeed item : listSingle){
           System.out.println("Date: " + item.date + " has: " + item.getAllCheckPoint().size() +" checkpoints: "+item.getAllCheckPoint());
           ArrayList<SingleListSpeed> lstSubSeq = item.findAllSubSequential();
           
           for(SingleListSpeed seq : lstSubSeq){
               ArrayList<String> lstStr = seq.createLookBackData(LOOK_BACK);
               dataLookBack.add(lstStr);
           }
        }
        
        BufferedWriter bw = null;
	FileWriter fw = null;
        fw = new FileWriter(outFileName);
        bw = new BufferedWriter(fw);
        
        // Write Header
        String wHeader="";
        for(int k = 0; k < LOOK_BACK; k++){
            wHeader = wHeader + "frame"+k+",speed" + k + ",";
        }
        wHeader = wHeader + "predictedSpeed";
        bw.write(wHeader);
        bw.newLine();
        // Write data to file
        for(ArrayList<String> item : dataLookBack){
            if(item != null){
                for(String result: item){
                    String [] wArr = result.split(",");
                    String wResult = "";
                    for(int u = 0; u < LOOK_BACK; u++){
                        wResult = wResult+wArr[3*u + 1] + ",";
                        wResult = wResult+wArr[3*u + 2] + ",";
                    }
                    wResult = wResult+wArr[wArr.length-1];

                    bw.write(wResult);
                    bw.newLine();
                }
            }
        }      
        bw.close();
        fw.close();   
    }
}
