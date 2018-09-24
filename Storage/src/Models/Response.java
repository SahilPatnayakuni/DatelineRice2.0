package Models;

/**
 * Created by lucy and ameesh on 9/24/18.
 */
public class Response {

    public Response(
        String status,
        String responseMessage
    ) throws Exception {
        this.status = status;
        this.responseMessage = responseMessage;
    }

    private String status;
    private String responseMessage;

    
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getResponseMessage() {
        return responseMessage;
    }

    public void setResponseMessage(String responseMessage) {
        this.responseMessage = responseMessage;
    }

}
