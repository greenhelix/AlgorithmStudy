public class ExploringTheWaters {
    public static void main(String[] args){
       
}
    String[] addBorder(String[] picture){
        String[] star = new String [picture.length +2];

        for(int i =0; i < picture.length; i++)
           { star[i+1] = "*" + picture[i] + "*"; 
             star[0] = star[1].replaceAll(".", "*");
             star[picture.length +1] = star[0]; }

        return star; 
    }

}