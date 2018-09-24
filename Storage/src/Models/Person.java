package Models;
import util.CustomTypes.*;

import java.util.UUID;

/**
 * Created by lucyfox on 9/24/18.
 */
public class Person {

    public Person(
        String net_id,
        String first_name,
        String last_name,
        String title,
        PersonType type,
        String[] organizations,
        String residential_college,
        String[] majors,
        Boolean is_former,
        Integer graduation_year
    ) throws Exception {
        this.net_id = net_id;
        this.first_name = first_name;
        this.last_name = last_name;
        this.title = title;
        this.type = type;
        this.organizations = organizations;
        this.residential_college = residential_college;
        this.majors = majors;
        this.is_former = is_former;
        this.graduation_year = graduation_year;
    }

    private String net_id;

    private String first_name;

    private String last_name;

    private String title;

    private PersonType type;

    private String[] organizations;

    private String residential_college;

    private String[] majors;

    private Boolean is_former;

    private Integer graduation_year;

    public String getNet_id() {
        return net_id;
    }

    public void setNet_id(String net_id) {
        this.net_id = net_id;
    }

    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public PersonType getType() {
        return type;
    }

    public void setType(PersonType type) {
        this.type = type;
    }

    public String[] getOrganizations() {
        return organizations;
    }

    public void setOrganizations(String[] organizations) {
        this.organizations = organizations;
    }

    public String getResidential_college() {
        return residential_college;
    }

    public void setResidential_college(String residential_college) {
        this.residential_college = residential_college;
    }

    public String[] getMajors() {
        return majors;
    }

    public void setMajors(String[] majors) {
        this.majors = majors;
    }

    public Boolean getIs_former() {
        return is_former;
    }

    public void setIs_former(Boolean is_former) {
        this.is_former = is_former;
    }

    public Integer getGraduation_year() {
        return graduation_year;
    }

    public void setGraduation_year(Integer graduation_year) {
        this.graduation_year = graduation_year;
    }
}
