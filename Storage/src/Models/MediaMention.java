package Models;

import java.sql.Timestamp;

/**
 * Created by lucy and ameesh on 9/23/18.
 */
public class MediaMention {

    enum MediaType {
        WEB, NEWSPAPER, RADIO, TV
    }

    enum Scope {
        NATIONAL, INTERNATIONAL, LOCAL
    }

    enum Category {
        FEATURED, NATIONAL_INTERNATIONAL, HOUSTON_TEXAS,
        BROADCAST, TRADE_PROFESSONAL, OTHER_NEWS, SPORTS
    }

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

}
