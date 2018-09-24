package Models;
import util.CustomTypes.*;

import java.sql.Timestamp;

/**
 * Created by lucy and ameesh on 9/23/18.
 */
public class MediaMention {

    public MediaMention(
        String headline,
        String outletName,
        MediaType mediaType,
        Scope scope,
        String locale,
        String language,
        Timestamp coverageDate,
        Timestamp datelineDate,
        Category category
    ) throws Exception {
        this.headline = headline;
        this.outletName = outletName;
        this.mediaType = mediaType;
        this.scope = scope;
        this.locale = locale;
        this.language = language;
        this.coverageDate = coverageDate;
        this.datelineDate = datelineDate;
        this.category = category;
    }

    private String headline;

    private String outletName;

    private MediaType mediaType;

    private Scope scope;

    private String locale;

    private String language;

    private Timestamp coverageDate;

    private Timestamp datelineDate;

    private Category category;

    public String getHeadline() {
        return headline;
    }

    public void setHeadline(String headline) {
        this.headline = headline;
    }

    public String getOutletName() {
        return outletName;
    }

    public void setOutletName(String outletName) {
        this.outletName = outletName;
    }

    public MediaType getMediaType() {
        return mediaType;
    }

    public void setMediaType(MediaType mediaType) {
        this.mediaType = mediaType;
    }

    public Scope getScope() {
        return scope;
    }

    public void setScope(Scope scope) {
        this.scope = scope;
    }

    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public Timestamp getCoverageDate() {
        return coverageDate;
    }

    public void setCoverageDate(Timestamp coverageDate) {
        this.coverageDate = coverageDate;
    }

    public Timestamp getDatelineDate() {
        return datelineDate;
    }

    public void setDatelineDate(Timestamp datelineDate) {
        this.datelineDate = datelineDate;
    }

    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }
}
