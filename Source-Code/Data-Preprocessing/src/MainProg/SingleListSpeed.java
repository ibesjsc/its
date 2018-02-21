/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package MainProg;

import java.util.ArrayList;
import java.util.Collections;

/**
 *
 * @author Luzec
 */
public class SingleListSpeed {
    public ArrayList<SpeedItem> lstSpeed;
    public String date; 
    public SingleListSpeed(String _date){
        date = _date;
        lstSpeed = new ArrayList<SpeedItem>();
    }
    
    public ArrayList<Integer> getAllCheckPoint(){
        ArrayList<Integer> lstCheckPoint = new ArrayList<Integer>();
        
        Collections.sort(lstSpeed);
        
        int currentTrack = 0;
        
        for(SpeedItem item : lstSpeed){
            if(lstCheckPoint.isEmpty()){
                currentTrack = item.frame;
                lstCheckPoint.add(item.frame);
            }
            else{
                if(item.frame - currentTrack == 1){
                    currentTrack ++;
                }
                else{
                    currentTrack = item.frame;
                    lstCheckPoint.add(item.frame);
                }
            }
        }
        return lstCheckPoint;
    }
    
    public SpeedItem find(int _frame){
        for(SpeedItem item : this.lstSpeed){
            if(item.frame == _frame){
                return item;
            }
        }
        return null;
    }
    
    public ArrayList<SingleListSpeed> findAllSubSequential(){
        ArrayList<SingleListSpeed> listSubSeq = new ArrayList<SingleListSpeed>();
        
        ArrayList<Integer> allCheckPoint = this.getAllCheckPoint();
        
        for(int i:allCheckPoint){
            SingleListSpeed lst = new SingleListSpeed(this.date);
            int current = i;
            SpeedItem sp = this.find(current);
            while(sp!=null){
                lst.lstSpeed.add(sp);
                current = current + 1;
                sp = this.find(current);
            }  
            Collections.sort(lst.lstSpeed);
            listSubSeq.add(lst);
        }
        
        // Test length
        int result = 0;
        for(SingleListSpeed item : listSubSeq){
            result = result + item.lstSpeed.size();
        }
        
        System.out.println("Length all sub: " + result);
        
        return listSubSeq;
    }
   
    public ArrayList<String> createLookBackData(int look_back){
        
        ArrayList<String> lstStringLookBack = new ArrayList<String>();
        
        if(this.lstSpeed.size() < look_back){
            return null;
        }
        else{
            for(int i = 0 ; i < this.lstSpeed.size(); i++){
                String result = "";
                if(i+ look_back < this.lstSpeed.size()){
                    for(int j  = i; j < i+ look_back; j++){
                        result = result + this.lstSpeed.get(j).toString() + ",";
                    }
                    result = result + this.lstSpeed.get(i+ look_back).speed;
                    lstStringLookBack.add(result);
                }
                else{
                    break;
                }
            }
        }   
        return lstStringLookBack;
    }
}
