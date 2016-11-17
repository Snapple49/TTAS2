#!/usr/bin/python
import interface as i

i.sign_on(8,"01")
i.open_acc()
i.art_reg(59922827)
i.art_reg(20013226, 3)
i.close_acc()
i.trans("tm_cash")
i.idle()
i.quit()
i.flush()