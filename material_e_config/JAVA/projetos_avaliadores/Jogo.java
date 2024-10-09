import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.io.IOException;


public class Jogo {
    public static void main(String[] args) throws IOException {
        Path fonte = Path.of("C:\\Users\\User\\IdeaProjects\\jogoForca\\src\\palavras.txt");
        List<String> palavras = Files.readAllLines(fonte);
        double randomIndex = Math.random() * palavras.size() - 1;
        int i = (int) randomIndex;
        String palavra = palavras.get(i);
        Scanner leitor = new Scanner(System.in);
        char[] estrutura = new char[palavra.length()];
        Arrays.fill(estrutura, '-');
        int forca = 0;
        String[] estruturaforca = palavra.split("");
        String palpite;
        while (forca != 6) {
            System.out.println(estrutura);
            System.out.println("Digite uma letra:");
            palpite = leitor.next();
            int cont = 0;
            for (int j = 0; j < palavra.length(); j++) {
                if (palpite.equalsIgnoreCase(estruturaforca[j])) {
                    estrutura[j] = palavra.charAt(j);
                    cont = 1;
                }
            }
            if (cont == 0 ) {
                forca++;
                System.out.println("forca: " + forca);
            }
            if (forca == 6) {
                System.out.println("Você morreu! tente novamente\n" +
                        "A palavra era: " + Arrays.toString(palavra.split(",")));
            }
            int fim = 0;
            boolean boleano = true;
            for (int j=0; j<palavra.length();j++){
                if (estrutura[palavra.length() - 1] != '-' && boleano){
                    ++fim;
                    boleano =false;
                }
                if (estrutura[j] != '-'){
                    ++fim;


                }
            }
            if (fim == palavra.length()+1){
                System.out.println("Parabéns, você acertou a palavra!");
                return;
            }
        }
    }
}
