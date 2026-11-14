import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

/**
 * The Main class implements an application that reads lines from the standard input
 * and prints them to the standard output.
 */
public class Main {

  // DO NOT MODIFY: Main method to read input and produce output
  public static void main(String[] args) throws IOException {
    try {
      // DO NOT MODIFY: Parse input into List of Client objects
      List<Client> clients = parseInput(
        new BufferedReader(
          new InputStreamReader(System.in, StandardCharsets.UTF_8)
        )
      );
      // DO NOT MODIFY: Process the Request object to create a Response object
      List<Signer> signers = processClients(clients);
      // DO NOT MODIFY: Validate signers is not null (can be an empty list)
      if (signers == null) {
        throw new IllegalStateException("Error processing list of clients");
      }
      // DO NOT MODIFY: Format and print the Response object to standard output
      System.out.println(formatOutput(signers));
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }
  }

  // TODO: Your processing logic here to create list of Signer objects
  private static List<Signer> processClients(List<Client> clients) {
    List<Signer> signers = new ArrayList<>();
    if (clients == null) {
      return signers;
    }

    int order = 1;
    for (Client client : clients) {
      boolean isEligibleSigner =
        !client.isCompany() &&
        client.isNamedInsured() &&
        client.isEmailPreferred() &&
        isValidEmail(client.getEmailAddress());

      if (isEligibleSigner) {
        signers.add(new Signer(client.getId(), order++));
      }
    }

    return signers;
  }

  // ### DO NOT MODIFY SECTION BELOW #############################################

  // DO NOT MODIFY: Checks if an email address is valid
  private static boolean isValidEmail(String email) {
    return (
      email != null &&
      Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$").matcher(email).matches()
    );
  }

  // DO NOT MODIFY: Formats output string given a list of signers
  private static String formatOutput(List<Signer> signers) {
    StringBuilder out = new StringBuilder();
    out
      .append("eligible:")
      .append(!signers.isEmpty() ? "true" : "false")
      .append(System.lineSeparator());
    out
      .append("signers:")
      .append(signers.size())
      .append(System.lineSeparator());
    for (Signer signer : signers) {
      out
        .append("signer:")
        .append(signer.getId())
        .append(System.lineSeparator());
      out
        .append("order:")
        .append(signer.getOrder())
        .append(System.lineSeparator());
      out
        .append("tags:")
        .append(signer.getTags().size())
        .append(System.lineSeparator());
      out
        .append("tag:")
        .append("signature:")
        .append(signer.getTags().get("signature"))
        .append(System.lineSeparator());
      out
        .append("tag:")
        .append("date:")
        .append(signer.getTags().get("date"))
        .append(System.lineSeparator());
    }
    return out.toString();
  }

  // DO NOT MODIFY: Reads input into a list of clients
  private static List<Client> parseInput(BufferedReader reader) {
    List<Client> clients = new ArrayList<>();
    try {
      int clientCount = Integer.parseInt(
        reader.readLine().substring("clients:".length())
      );
      for (int i = 0; i < clientCount; i++) {
        List<String> roles = new ArrayList<>();
        String clientId = reader.readLine().substring("client:".length());
        String emailAddress = reader
          .readLine()
          .substring("email-address:".length());
        boolean emailPreference = Boolean.parseBoolean(
          reader.readLine().substring("email-preference:".length())
        );
        int roleCount = Integer.parseInt(
          reader.readLine().substring("roles:".length())
        );
        for (int j = 0; j < roleCount; j++) {
          roles.add(reader.readLine().substring("role:".length()));
        }
        clients.add(new Client(clientId, emailAddress, emailPreference, roles));
      }
    } catch (IOException e) {
      System.out.println(e.getMessage());
    }
    return clients;
  }

  // DO NOT MODIFY: Client object to hold client data
  public static class Client {

    private final String id;
    private final String emailAddress;
    private final boolean emailPreference;
    private final List<String> roles;

    public Client(
      String id,
      String emailAddress,
      boolean emailPreference,
      List<String> roles
    ) {
      this.id = id;
      this.emailAddress = emailAddress;
      this.emailPreference = emailPreference;
      this.roles = roles;
    }

    public String getId() {
      return id;
    }

    public String getEmailAddress() {
      return emailAddress;
    }

    public boolean isEmailPreferred() {
      return emailPreference;
    }

    public boolean isCompany() {
      return containsRole("company");
    }

    public boolean isPrimaryNamedInsured() {
      return containsRole("primary-named-insured");
    }

    public boolean isAdditionalNamedInsured() {
      return containsRole("additional-named-insured");
    }

    public boolean isNamedInsured() {
      return isPrimaryNamedInsured() || isAdditionalNamedInsured();
    }

    private boolean containsRole(String value) {
      return roles.contains(value);
    }
  }

  // DO NOT MODIFY: Signer object to hold signer data
  public static class Signer {

    private final String id;
    private final int order;
    private final Map<String, String> tags;

    public Signer(String id, int order) {
      this.id = id;
      this.order = order;
      this.tags = Map.of(
        "signature",
        createTag("#$S", order),
        "date",
        createTag("#$D", order)
      );
    }

    private static String createTag(String prefix, int order) {
      return String.format("%s%02d", prefix, order);
    }

    public String getId() {
      return id;
    }

    public int getOrder() {
      return order;
    }

    public Map<String, String> getTags() {
      return tags;
    }
  }
}
