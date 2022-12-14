module.exports = {
    types: [
        {
            value: 'ð feat',
            name: 'feat: æ©è½è¿½å ',
            title: 'Features',
        },
        {
            value: 'ð§ fix',
            name: 'fix: ãã°ã®ä¿®æ­£',
            title: 'Bug Fixes',
        },
        {
            value: 'ð docs',
            name: 'docs: ãã­ã¥ã¡ã³ãã®ã¿ã®å¤æ´',
            title: 'Documentation',
        },
        {
            value: 'ð¨ style',
            name: 'style: ã³ã¼ãã®åä½ã«å½±é¿ããªããè¦ãç®ã ãã®å¤æ´ï¼ã¹ãã¼ã¹ããã©ã¼ããããæ¬ è½ã®ä¿®æ­£ãã»ãã³ã­ã³ãªã©)',
            title: 'Styles',
        },
        {
            value: 'â»ï¸ refactor',
            name: 'refactor: ãã°ã®ä¿®æ­£ãæ©è½ã®è¿½å ã§ã¯ãªãã³ã¼ãã®å¤æ´',
            title: 'Code Refactoring',
        },
        {
            value: 'â«ãperf',
            name: 'perf: ããã©ã¼ãã³ã¹ãåä¸ãããã³ã¼ãã®å¤æ´',
            title: 'Performance',
        },
        {
            value: 'ð§ª test',
            name: 'test: ä¸è¶³ãã¦ãããã¹ãã®è¿½å ãæ¢å­ã®ãã¹ãã®ä¿®æ­£',
            title: 'Tests',
        },
        {
            value: 'ð§ chore',
            name: 'chore: ãã«ããã­ã»ã¹ããã­ã¥ã¡ã³ãçæãªã©ã®è£å©ãã¼ã«ãã©ã¤ãã©ãªã®å¤æ´',
            title: 'Chores',
        },
    ],
    messages: {
        type: 'ã³ãããããå¤æ´ã¿ã¤ããé¸æãã¦ãã ãã:\n',
        subject: 'ã³ãããåå®¹ã«ã¤ãã¦å¥åãã¦ãã ãã:\n',
        confirmCommit: 'ãã¡ãã®åå®¹ã§ã³ããããå®è¡ãã¦ããããã§ããï¼:\n',
        /* ticketNumber: 'ãã±ããçªå·ãå¥åãã¦ãã ãã (ãªãå ´åã¯Enter):\n',*/
    },
    skipQuestions: ['scope', 'body', 'breaking', 'footer'],
    allowBreakingChanges: ['feat', 'fix'],
    /*
    ã³ãããã¡ãã»ã¼ã¸ã«ãã±ããçªå·ãè¿½å ãããå ´åã³ã¡ã³ããåé¤
    allowTicketNumber: true,
    isTicketNumberRequired: false,
    ticketNumberPrefix: '',
    ticketNumberRegExp: '',
    */
}