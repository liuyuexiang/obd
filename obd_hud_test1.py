
import obd
import log

# connection = obd.OBD()
for command in obd.commands.modes[1]:
    # print(command.name + '|' + command.desc + '|' + str(command.command))
    log.PlatformLog.info('指令%s描述%s',command.name ,command.desc)
#     c = command.name
#     response = connection.query(c)
#     print(command.desc,response.value)
# connection.close()