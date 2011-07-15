# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc, OpenERP Professional Services   
#    Copyright (C) 2010-2011 Avanzosc S.L (http://www.avanzosc.com). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class dayly_part(osv.osv):

    _name = 'dayly.part'
    _description = 'Farm Dayly Part'
 
    _columns = {
            'location_id': fields.many2one('stock.location', 'Location', domain=[('usage', '=', 'internal')]),
            'date': fields.date('Date'),
            'prodlot_id': fields.many2one('stock.production.lot', 'Lot'),
            'machine_eggs': fields.float('Machine Eggs'),
            'dirty_eggs': fields.float('Dirty Eggs'),
            'broken_eggs': fields.float('Broken Eggs'),
            'machine_broke_eggs': fields.float('Machine Broken Eggs'),
            'lecture_date': fields.date('Lecture Date'),
            'water_lecture': fields.float('Water Lecture'),
            'water_consum': fields.float('Water Consumtion'),
            'water_price': fields.float('Water Price'),
            'max_temp': fields.float('Max. Temperature'),
            'min_temp': fields.float('Min. Temperature'),
    }
dayly_part()