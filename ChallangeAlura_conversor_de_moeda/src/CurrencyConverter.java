import java.io.IOException;

import java.net.URI;

import java.net.http.HttpClient;

import java.net.http.HttpRequest;

import java.net.http.HttpResponse;

import java.util.HashMap;

import java.util.Map;

import java.util.Scanner;

import com.google.gson.JsonObject;

import com.google.gson.JsonParser;

public class CurrencyConverter {

    private static final String API_KEY = "18cbf7e5ea48150e687ce8fa";

    private static final String BASE_URL = "https://v6.exchangerate-api.com/v6/" + "18cbf7e5ea48150e687ce8fa" + "/latest/USD";

    private static Map<String, Double> exchangeRates = new HashMap<>();

    public static void main(String[] args) {

        try {

            fetchExchangeRates();

            Scanner scanner = new Scanner(System.in);

            while (true) {

                System.out.println("Seja Bem Vindo/a ao conversor de moeda.");

                System.out.println("1) Dolar => Peso Argentino");

                System.out.println("2) Peso Argentino => Dolar");

                System.out.println("3) Dolar => Real Brasileiro");

                System.out.println("4) Real Brasileiro => Dólar");

                System.out.println("5) Dolar => Kwanza Angolano");

                System.out.println("6) Kwanza Angolano => Dólar");

                System.out.println("7) Real Brasileiro => Kwanza Angolano");

                System.out.println("8) Kwanza Angolano => Real Brasileiro");

                System.out.println("9) Sair");

                System.out.print("Escolha uma opção: ");

                int option = scanner.nextInt();

                if (option == 9) {

                    System.out.println("Saindo...");

                    break;

                }

                System.out.print("Digite o valor a ser convertido: ");

                double amount = scanner.nextDouble();

                double convertedAmount = 0;

                switch (option) {

                    case 1:

                        convertedAmount = convert(amount, "USD", "ARS");

                        System.out.println("Valor em Peso Argentino: " + convertedAmount + " ARS");

                        break;

                    case 2:

                        convertedAmount = convert(amount, "ARS", "USD");

                        System.out.println("Valor em Dólar: " + convertedAmount+" USD");

                        break;

                    case 3:

                        convertedAmount = convert(amount, "USD", "BRL");

                        System.out.println("Valor em Real Brasileiro: " + convertedAmount + " BRL");

                        break;

                    case 4:

                        convertedAmount = convert(amount, "BRL", "USD");

                        System.out.println("Valor em Dólar: " + convertedAmount + " USD");

                        break;

                    case 5:

                        convertedAmount = convert(amount, "USD", "AOA");

                        System.out.println("Valor em Kwanza Angolano: " + convertedAmount + " AOA");

                        break;

                    case 6:

                        convertedAmount = convert(amount, "AOA", "USD");

                        System.out.println("Valor em Dólar: " + convertedAmount + " USD");

                        break;

                    case 7:

                        convertedAmount = convert(amount, "BRL", "AOA");

                        System.out.println("Valor em Kwanza Angolano: " + convertedAmount + " AOA");

                        break;

                    case 8:

                        convertedAmount = convert(amount, "AOA", "BRL");

                        System.out.println("Valor em Real Brasileiro: " + convertedAmount + " BRL");

                        break;

                    default:

                        System.out.println("Opção inválida.");

                }

                System.out.println();

            }

            scanner.close();

        } catch (IOException | InterruptedException e) {

            e.printStackTrace();

        }

    }

    private static void fetchExchangeRates() throws IOException, InterruptedException {

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()

                .uri(URI.create(BASE_URL))

                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        JsonObject jsonResponse = JsonParser.parseString(response.body()).getAsJsonObject();

        if (jsonResponse.get("result").getAsString().equals("success")) {

            JsonObject rates = jsonResponse.getAsJsonObject("conversion_rates");

            exchangeRates.put("ARS", rates.get("ARS").getAsDouble());

            exchangeRates.put("BRL", rates.get("BRL").getAsDouble());

            exchangeRates.put("AOA", rates.get("AOA").getAsDouble());

            exchangeRates.put("USD", rates.get("USD").getAsDouble());

        } else {

            System.out.println("Erro ao obter as taxas de câmbio.");

        }

    }

    private static double convert(double amount, String fromCurrency, String toCurrency) {

        double fromRate = exchangeRates.get(fromCurrency);

        double toRate = exchangeRates.get(toCurrency);

        return amount * (toRate / fromRate);

    }

}