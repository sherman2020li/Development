extern void cxpi_frame_process(U8 RefID);
extern void ld_send_messasge(U8 RefID);
extern void ld_receive_messasge(U8 RefID);
extern void ld_process_pid(U8 pid);
extern void ld_process_parity(U8 pid);
extern void ld_process_frameinfo(U8 refID);
extern STA ld_calc_crc(U8 crc);
extern U8 cxpi_receive_data_compelted_callback();

