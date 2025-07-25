# This file contains all the static data for the game world.

GAME_MAP = {
    'slags_alley': {
        'name': "یک کوچه پس‌کوچه کثیف",
        'desc': "با بوی تند شراب ترشیده و زباله از خواب بیدار می‌شوی. تو در کوچه‌ای باریک و گلی، در اعماق شهر هستی. نردبان‌های چوبی لرزان از دیوارهای آجری و نم‌زده بالا رفته‌اند. تنها راه خروج، شکافی باریک به سمت خیابانی شلوغ به نظر می‌رسد.",
        'exits': {'خیابان': 'rookery_entrance'}
    },
    'rookery_entrance': {
        'name': "ورودی زاغه‌نشین",
        'desc': "تو در آستانه زاغه‌نشین ایستاده‌ای، هزارتویی از خانه‌های در حال فروریختن و کوچه‌های تاریک. هوا از دود زغال‌سنگ و بوی ناامیدی سنگین است. به سمت شمال، کوچه‌ها تنگ‌تر می‌شوند. در شرق، هیاهوی یک بازار بزرگ به گوش می‌رسد. در غرب، دیوارهای مستحکم محله آهن را می‌بینی. خیابانی کثیف به سمت جنوب و به دل زاغه‌ها بازمی‌گردد.",
        'exits': {'شمال': 'rookery_depths', 'شرق': 'gilded_market_gate', 'غرب': 'iron_quarter_gate', 'جنوب': 'slags_alley'}
    },
    'rookery_depths': {
        'name': "اعماق زاغه‌نشین",
        'desc': "تو در قلب قلمرو دزدان هستی. نجواهایی از درگاه‌های تاریک به گوش می‌رسد و چشمانی از پشت پنجره‌های چرک‌آلود تو را می‌پایند. اینجا قلمرو سندیکای سایه است. کوچه‌ای به خصوص تاریک به یک سرداب مخفی منتهی می‌شود.",
        'exits': {'جنوب': 'rookery_entrance', 'سرداب': 'syndicate_hideout'}
    },
    'syndicate_hideout': {
        'name': "مخفیگاه سندیکای سایه",
        'desc': "میکده‌ای در یک سرداب که با چراغ‌های دزدی روشن شده است. دزدان و قاتلان زیر لب با هم صحبت می‌کنند، اما با ورود تو سکوت می‌کنند. زنی با صورتی زخمی از پشت پیشخوان با سوءظن به تو می‌نگرد. اینجا مکانی برای فرصت‌های خطرناک است.",
        'exits': {'بالا': 'rookery_depths'}
    },
    'gilded_market_gate': {
        'name': "دروازه بازار زرین",
        'desc': "هرج‌ومرج زاغه‌نشین جای خود را به انرژی پر جنب‌وجوش بازار زرین می‌دهد. بوی ادویه‌های عجیب، دام‌ها و پول در هوا پیچیده است. نگهبانانی که توسط کنسرسیوم تجاری استخدام شده‌اند، هر کسی را که وارد می‌شود زیر نظر دارند.",
        'exits': {'غرب': 'rookery_entrance', 'داخل': 'gilded_market_square'}
    },
    'gilded_market_square': {
        'name': "میدان بازار زرین",
        'desc': "قلب تپنده تجارت خاکستران. غرفه‌ها مملو از کالاهایی از سراسر قلمرو هستند. بازرگانان کالاهای خود را فریاد می‌زنند و مزدوران شمشیرهای خود را برای سکه عرضه می‌کنند. ثروت شهر از اینجا جریان دارد.",
        'exits': {'دروازه': 'gilded_market_gate'}
    },
    'iron_quarter_gate': {
        'name': "دروازه محله آهن",
        'desc': "دروازه‌ای عظیم از آهن و سنگ، ورودی منطقه نظامی شهر را مشخص می‌کند. وفاداران گریفین با چهره‌های سخت و عبوس نگهبانی می‌دهند. زره‌هایشان صیقلی است، اما چشمانشان خسته. آن‌ها آخرین سنگر نظم قدیم هستند.",
        'exits': {'شرق': 'rookery_entrance', 'داخل': 'iron_quarter_barracks'}
    },
    'iron_quarter_barracks': {
        'name': "پادگان محله آهن",
        'desc': "حیاط پادگان صحنه‌ای از فعالیت منظم است. سربازان با شمشیر تمرین می‌کنند، زره تعمیر می‌کنند و نقشه‌ها را مطالعه می‌کنند. صدای فولاد و فریادهای دستوری در هوا طنین‌انداز است. اینجا مرکز فرماندهی تلاش وفاداران گریفین برای بازپس‌گیری شهر است.",
        'exits': {'دروازه': 'iron_quarter_gate'}
    },
}

FACTIONS = {
    'syndicate': {
        'name': "سندیکای سایه",
        'desc': "یک اتحادیه عمل‌گرا و بی‌رحم از دزدان و آدم‌کشان. آن‌ها به دنبال حکومت بر شهر نیستند، فقط می‌خواهند خون آن را بمکند."
    },
    'loyalists': {
        'name': "وفاداران گریفین",
        'desc': "بقایای گارد آهنین شهر که به خاطره دوک و آرمان نظم وفادار مانده‌اند. منظم و مجهز، اما با کمبود نیرو مواجه‌اند."
    },
    'consortium': {
        'name': "کنسرسیوم تجاری",
        'desc': "شورایی از ثروتمندترین بازرگانان شهر. آن‌ها از ثروت خود به عنوان سلاح استفاده می‌کنند و برای حفاظت از خود مزدور استخدام می‌کنند."
    }
}
