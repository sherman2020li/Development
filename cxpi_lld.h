extern void cxpi_initialization(void);
extern STA set_baudrate(U8 RefID);
extern U16 get_baudrate(U8 RefID);
extern void lld_enable_Clock(void);
extern void lld_disable_Clock(void);
extern void lld_uart(void);
extern void enable_interrupt(void);
extern void disable_interrupt(void);

